import pandas as pd
from sqlalchemy import create_engine

class SQLiteMemory:
    def __init__(self, db_path="memory.db"):
        self.engine = create_engine(f"sqlite:///{db_path}")
        self._init_db()

    def _init_db(self):
        with self.engine.connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS memory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    prompt TEXT,
                    code TEXT,
                    output TEXT
                );
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS df_last (
                    id INTEGER PRIMARY KEY,
                    data BLOB
                );
            """)

    def save_turn(self, prompt, code, output, df_last=None):
        with self.engine.begin() as conn:
            conn.execute(
                "INSERT INTO memory (prompt, code, output) VALUES (?, ?, ?);",
                (prompt, code, output)
            )
            if df_last is not None:
                df_last.to_pickle("df_last.pkl")
                conn.execute("DELETE FROM df_last;")
                conn.execute(
                    "INSERT INTO df_last (id, data) VALUES (?, ?);",
                    (1, open("df_last.pkl", "rb").read())
                )

    def load_memory(self):
        return pd.read_sql("SELECT * FROM memory", self.engine).to_dict(orient="records")

    def load_df_last(self):
        try:
            with self.engine.connect() as conn:
                result = conn.execute("SELECT data FROM df_last WHERE id = 1;").fetchone()
                if result:
                    with open("df_last.pkl", "wb") as f:
                        f.write(result[0])
                    return pd.read_pickle("df_last.pkl")
        except Exception:
            return None

    def clear_memory(self):
        with self.engine.begin() as conn:
            conn.execute("DELETE FROM memory;")
            conn.execute("DELETE FROM df_last;")
