// LeetCode 1890 - The Latest Login In 2020
// https://leetcode.com/problems/the-latest-login-in-2020/

let QUERY = """
SELECT user_id, MAX(time_stamp) AS last_stamp
FROM Logins
WHERE time_stamp >= '2020-01-01' AND time_stamp < '2021-01-01'
GROUP BY user_id;
"""
