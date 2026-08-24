// LeetCode 1127 - User Purchase Platform
// https://leetcode.com/problems/user-purchase-platform/

class Solution {
    companion object {
        const val QUERY = "WITH dates AS (\n" +
            "    SELECT DISTINCT spend_date FROM Spending\n" +
            "),\n" +
            "platforms AS (\n" +
            "    SELECT 'desktop' AS platform\n" +
            "    UNION ALL SELECT 'mobile'\n" +
            "    UNION ALL SELECT 'both'\n" +
            "),\n" +
            "user_flags AS (\n" +
            "    SELECT\n" +
            "        spend_date,\n" +
            "        user_id,\n" +
            "        SUM(platform = 'desktop') AS has_desktop,\n" +
            "        SUM(platform = 'mobile') AS has_mobile,\n" +
            "        SUM(amount) AS total_amount\n" +
            "    FROM Spending\n" +
            "    GROUP BY spend_date, user_id\n" +
            ")\n" +
            "SELECT\n" +
            "    d.spend_date,\n" +
            "    p.platform,\n" +
            "    COALESCE(SUM(CASE\n" +
            "        WHEN p.platform = 'desktop' AND uf.has_desktop = 1 AND uf.has_mobile = 0 THEN uf.total_amount\n" +
            "        WHEN p.platform = 'mobile' AND uf.has_mobile = 1 AND uf.has_desktop = 0 THEN uf.total_amount\n" +
            "        WHEN p.platform = 'both' AND uf.has_desktop = 1 AND uf.has_mobile = 1 THEN uf.total_amount\n" +
            "        ELSE 0\n" +
            "    END), 0) AS total_amount,\n" +
            "    COALESCE(SUM(CASE\n" +
            "        WHEN p.platform = 'desktop' AND uf.has_desktop = 1 AND uf.has_mobile = 0 THEN 1\n" +
            "        WHEN p.platform = 'mobile' AND uf.has_mobile = 1 AND uf.has_desktop = 0 THEN 1\n" +
            "        WHEN p.platform = 'both' AND uf.has_desktop = 1 AND uf.has_mobile = 1 THEN 1\n" +
            "        ELSE 0\n" +
            "    END), 0) AS total_users\n" +
            "FROM dates d\n" +
            "CROSS JOIN platforms p\n" +
            "LEFT JOIN user_flags uf ON d.spend_date = uf.spend_date\n" +
            "GROUP BY d.spend_date, p.platform"
    }
}
