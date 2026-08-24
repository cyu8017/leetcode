// LeetCode 1811 - Find Interview Candidates
// https://leetcode.com/problems/find-interview-candidates/

let QUERY = """
WITH Medals AS (
    SELECT contest_id, gold_medal AS user_id FROM Contests
    UNION ALL
    SELECT contest_id, silver_medal FROM Contests
    UNION ALL
    SELECT contest_id, bronze_medal FROM Contests
),
DistinctMedals AS (
    SELECT DISTINCT user_id, contest_id FROM Medals
),
ConsecutiveWinners AS (
    SELECT user_id
    FROM (
        SELECT
            user_id,
            contest_id - ROW_NUMBER() OVER (
                PARTITION BY user_id ORDER BY contest_id
            ) AS grp
        FROM DistinctMedals
    ) t
    GROUP BY user_id, grp
    HAVING COUNT(*) >= 3
),
GoldWinners AS (
    SELECT gold_medal AS user_id
    FROM Contests
    GROUP BY gold_medal
    HAVING COUNT(*) >= 3
),
Candidates AS (
    SELECT user_id FROM ConsecutiveWinners
    UNION
    SELECT user_id FROM GoldWinners
)
SELECT u.name, u.mail
FROM Users u
JOIN Candidates c ON u.user_id = c.user_id;
"""
