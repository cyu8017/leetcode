// LeetCode 1141 - User Activity For The Past 30 Days I
// https://leetcode.com/problems/user-activity-for-the-past-30-days-i/

class Solution {
    companion object {
        const val QUERY = "SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users\n" +
            "FROM Activity\n" +
            "WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'\n" +
            "GROUP BY activity_date"
    }
}
