// LeetCode 3172 - Second Day Verification
// https://leetcode.com/problems/second-day-verification/

class Solution {
    companion object {
        const val QUERY = "SELECT user_id\n" +
            "FROM\n" +
            "    Emails AS e\n" +
            "    JOIN texts AS t\n" +
            "        ON e.email_id = t.email_id\n" +
            "        AND DATEDIFF(action_date, signup_date) = 1\n" +
            "        AND signup_action = 'Verified'\n" +
            "ORDER BY 1;"
    }
}
