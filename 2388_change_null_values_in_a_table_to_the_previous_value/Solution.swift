// LeetCode 2388 - Change Null Values In A Table To The Previous Value
// https://leetcode.com/problems/change-null-values-in-a-table-to-the-previous-value/

let QUERY = """
WITH
    S AS (
        SELECT *, ROW_NUMBER() OVER () AS rk
        FROM CoffeeShop
    ),
    T AS (
        SELECT
            *,
            SUM(
                CASE
                    WHEN drink IS NULL THEN 0
                    ELSE 1
                END
            ) OVER (ORDER BY rk) AS gid
        FROM S
    )
SELECT
    id,
    MAX(drink) OVER (
        PARTITION BY gid
        ORDER BY rk
    ) AS drink
FROM T
"""
