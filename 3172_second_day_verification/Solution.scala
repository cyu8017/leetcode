// LeetCode 3172 - Second Day Verification
// https:// leetcode.com/problems/second-day-verification/

object Solution {
  final val QUERY: String = """SELECT user_id
FROM
    Emails AS e
    JOIN texts AS t
        ON e.email_id = t.email_id
        AND DATEDIFF(action_date, signup_date) = 1
        AND signup_action = 'Verified'
ORDER BY 1;
"""
}
