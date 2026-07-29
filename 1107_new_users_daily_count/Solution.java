// LeetCode 1107 - New Users Daily Count
// https://leetcode.com/problems/new-users-daily-count/

class Solution {
    public static final String QUERY = """
WITH first_login AS (
    SELECT user_id, MIN(activity_date) AS login_date
    FROM Traffic
    WHERE activity = 'login'
    GROUP BY user_id
)
SELECT login_date, COUNT(*) AS user_count
FROM first_login
WHERE login_date BETWEEN '2019-04-01' AND '2019-06-30'
GROUP BY login_date
""";
}
