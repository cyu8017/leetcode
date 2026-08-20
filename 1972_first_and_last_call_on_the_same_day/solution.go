// LeetCode 1972 - First and Last Call On the Same Day
// https://leetcode.com/problems/first-and-last-call-on-the-same-day/

const QUERY = `
WITH s AS (
    SELECT caller_id, recipient_id, call_time FROM Calls
    UNION ALL
    SELECT recipient_id, caller_id, call_time FROM Calls
),
t AS (
    SELECT
        caller_id AS user_id,
        FIRST_VALUE(recipient_id) OVER (
            PARTITION BY DATE(call_time), caller_id
            ORDER BY call_time ASC
        ) AS first_peer,
        FIRST_VALUE(recipient_id) OVER (
            PARTITION BY DATE(call_time), caller_id
            ORDER BY call_time DESC
        ) AS last_peer
    FROM s
)
SELECT DISTINCT user_id
FROM t
WHERE first_peer = last_peer
`
