// LeetCode 1939 - Users That Actively Request Confirmation Messages
// https://leetcode.com/problems/users-that-actively-request-confirmation-messages/

export const QUERY = `SELECT DISTINCT c1.user_id
FROM Confirmations c1
JOIN Confirmations c2
  ON c1.user_id = c2.user_id
 AND c1.time_stamp < c2.time_stamp
 AND TIMESTAMPDIFF(SECOND, c1.time_stamp, c2.time_stamp) <= 24 * 60 * 60`;
