# LeetCode 1890 - The Latest Login in 2020
# https://leetcode.com/problems/the-latest-login-in-2020/

import sqlite3
from typing import Any

QUERY = """
SELECT user_id, MAX(time_stamp) AS last_stamp
FROM Logins
WHERE time_stamp >= '2020-01-01' AND time_stamp < '2021-01-01'
GROUP BY user_id;
"""


class Solution:
    def query(self, Logins: list[dict[str, Any]]) -> list[dict[str, Any]]:
        conn = sqlite3.connect(":memory:")
        conn.row_factory = sqlite3.Row
        try:
            conn.execute(
                "CREATE TABLE Logins (user_id INTEGER, time_stamp TEXT)"
            )
            conn.executemany(
                "INSERT INTO Logins (user_id, time_stamp) VALUES (?, ?)",
                [(row["user_id"], row["time_stamp"]) for row in Logins],
            )
            rows = conn.execute(QUERY).fetchall()
            result = [
                {"user_id": row["user_id"], "last_stamp": row["last_stamp"]}
                for row in rows
            ]
            return sorted(result, key=lambda row: row["user_id"])
        finally:
            conn.close()
