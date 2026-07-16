# LeetCode 1132 - Reported Posts II
# https://leetcode.com/problems/reported-posts-ii/

QUERY = """
WITH daily AS (
    SELECT
        action_date,
        COUNT(DISTINCT post_id) AS reported,
        COUNT(DISTINCT CASE WHEN r.post_id IS NOT NULL THEN a.post_id END) AS removed
    FROM Actions a
    LEFT JOIN Removals r ON a.post_id = r.post_id
    WHERE a.action = 'report' AND a.extra = 'spam'
    GROUP BY action_date
)
SELECT ROUND(AVG(removed * 100.0 / reported), 2) AS average_daily_percent
FROM daily
"""
