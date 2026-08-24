// LeetCode 3497 - Analyze Subscription Conversion
// https:// leetcode.com/problems/analyze-subscription-conversion/

object Solution {
  final val QUERY: String = """WITH
    T AS (
        SELECT user_id, activity_type, ROUND(SUM(activity_duration) / COUNT(1), 2) duration
        FROM UserActivity
        WHERE activity_type != 'cancelled'
        GROUP BY user_id, activity_type
    ),
    F AS (
        SELECT user_id, duration trial_avg_duration
        FROM T
        WHERE activity_type = 'free_trial'
    ),
    P AS (
        SELECT user_id, duration paid_avg_duration
        FROM T
        WHERE activity_type = 'paid'
    )
SELECT user_id, trial_avg_duration, paid_avg_duration
FROM
    F
    JOIN P USING (user_id)
ORDER BY 1;
"""
}
