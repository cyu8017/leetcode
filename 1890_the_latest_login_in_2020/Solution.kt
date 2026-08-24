// LeetCode 1890 - The Latest Login In 2020
// https://leetcode.com/problems/the-latest-login-in-2020/

class Solution {
    companion object {
        const val QUERY = "SELECT user_id, MAX(time_stamp) AS last_stamp\n" +
            "FROM Logins\n" +
            "WHERE time_stamp >= '2020-01-01' AND time_stamp < '2021-01-01'\n" +
            "GROUP BY user_id;"
    }
}
