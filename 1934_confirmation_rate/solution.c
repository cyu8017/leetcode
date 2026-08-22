// LeetCode 1934 - Confirmation Rate
// https://leetcode.com/problems/confirmation-rate/

const char* QUERY =
    "\n"
    "SELECT s.user_id,\n"
    "       ROUND(AVG(IF(c.action = 'confirmed', 1, 0)), 2) AS confirmation_rate\n"
    "FROM Signups s\n"
    "LEFT JOIN Confirmations c ON s.user_id = c.user_id\n"
    "GROUP BY s.user_id\n";
