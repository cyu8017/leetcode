# LeetCode 2688 - Find Active Users
# https:# leetcode.com/problems/find-active-users/

# Write your MySQL query statement below
QUERY = """
SELECT DISTINCT
    user_id
FROM Users
WHERE
    user_id IN (
        SELECT
            user_id
        FROM
            (
                SELECT
                    user_id,
                    created_at,
                    LAG(created_at, 1) OVER (
                        PARTITION BY user_id
                        ORDER BY created_at
                    ) AS prev_created_at
                FROM Users
            ) AS t
        WHERE DATEDIFF(created_at, prev_created_at) <= 7
    )
"""
