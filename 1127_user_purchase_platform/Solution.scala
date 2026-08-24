// LeetCode 1127 - User Purchase Platform
// https://leetcode.com/problems/user-purchase-platform/

object Solution {
  final val QUERY: String = """WITH dates AS (
    SELECT DISTINCT spend_date FROM Spending
),
platforms AS (
    SELECT 'desktop' AS platform
    UNION ALL SELECT 'mobile'
    UNION ALL SELECT 'both'
),
user_flags AS (
    SELECT
        spend_date,
        user_id,
        SUM(platform = 'desktop') AS has_desktop,
        SUM(platform = 'mobile') AS has_mobile,
        SUM(amount) AS total_amount
    FROM Spending
    GROUP BY spend_date, user_id
)
SELECT
    d.spend_date,
    p.platform,
    COALESCE(SUM(CASE
        WHEN p.platform = 'desktop' AND uf.has_desktop = 1 AND uf.has_mobile = 0 THEN uf.total_amount
        WHEN p.platform = 'mobile' AND uf.has_mobile = 1 AND uf.has_desktop = 0 THEN uf.total_amount
        WHEN p.platform = 'both' AND uf.has_desktop = 1 AND uf.has_mobile = 1 THEN uf.total_amount
        ELSE 0
    END), 0) AS total_amount,
    COALESCE(SUM(CASE
        WHEN p.platform = 'desktop' AND uf.has_desktop = 1 AND uf.has_mobile = 0 THEN 1
        WHEN p.platform = 'mobile' AND uf.has_mobile = 1 AND uf.has_desktop = 0 THEN 1
        WHEN p.platform = 'both' AND uf.has_desktop = 1 AND uf.has_mobile = 1 THEN 1
        ELSE 0
    END), 0) AS total_users
FROM dates d
CROSS JOIN platforms p
LEFT JOIN user_flags uf ON d.spend_date = uf.spend_date
GROUP BY d.spend_date, p.platform
"""
}
