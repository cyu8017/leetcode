// LeetCode 1435 - Create A Session Bar Chart
// https://leetcode.com/problems/create-a-session-bar-chart/

class Solution {
    companion object {
        const val QUERY = "WITH numbered AS (\n" +
            "    SELECT id, login_date,\n" +
            "           DATE_SUB(login_date, INTERVAL ROW_NUMBER() OVER\n" +
            "                    (PARTITION BY id ORDER BY login_date) DAY) AS grp\n" +
            "    FROM (SELECT DISTINCT id, login_date FROM Logins) d\n" +
            "),\n" +
            "active AS (\n" +
            "    SELECT id FROM numbered GROUP BY id, grp HAVING COUNT(*) >= 5\n" +
            ")\n" +
            "SELECT DISTINCT a.id, a.name\n" +
            "FROM Accounts a JOIN active x ON x.id = a.id\n" +
            "ORDER BY a.id"
    }
}
