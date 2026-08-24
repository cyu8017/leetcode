// LeetCode 1454 - Active Users
// https://leetcode.com/problems/active-users/

class Solution {
    companion object {
        const val QUERY = "SELECT DISTINCT a.id, a.name\n" +
            "FROM Accounts a\n" +
            "JOIN (\n" +
            "    SELECT id, DATE_SUB(login_date, INTERVAL DENSE_RANK() OVER\n" +
            "        (PARTITION BY id ORDER BY login_date) DAY) AS grp\n" +
            "    FROM (SELECT DISTINCT id, login_date FROM Logins) d\n" +
            ") x ON x.id = a.id\n" +
            "GROUP BY a.id, a.name, x.grp\n" +
            "HAVING COUNT(*) >= 5"
    }
}
