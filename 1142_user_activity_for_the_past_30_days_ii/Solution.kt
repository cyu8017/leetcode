// LeetCode 1142 - User Activity For The Past 30 Days Ii
// https://leetcode.com/problems/user-activity-for-the-past-30-days-ii/

class Solution {
    companion object {
        const val QUERY = "SELECT ROUND(IFNULL(COUNT(DISTINCT session_id) / COUNT(DISTINCT user_id), 0), 2) AS average_sessions_per_user\n" +
            "FROM Activity\n" +
            "WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'"
    }
}
