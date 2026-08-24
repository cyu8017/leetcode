// LeetCode 1107 - New Users Daily Count
// https://leetcode.com/problems/new-users-daily-count/

class Solution {
    companion object {
        const val QUERY = "WITH first_login AS (\n" +
            "    SELECT user_id, MIN(activity_date) AS login_date\n" +
            "    FROM Traffic\n" +
            "    WHERE activity = 'login'\n" +
            "    GROUP BY user_id\n" +
            ")\n" +
            "SELECT login_date, COUNT(*) AS user_count\n" +
            "FROM first_login\n" +
            "WHERE login_date BETWEEN '2019-04-01' AND '2019-06-30'\n" +
            "GROUP BY login_date"
    }
}
