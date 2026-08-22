// LeetCode 1939 - Users That Actively Request Confirmation Messages
// https://leetcode.com/problems/users-that-actively-request-confirmation-messages/

const char* QUERY =
    "\n"
    "SELECT DISTINCT c1.user_id\n"
    "FROM Confirmations c1\n"
    "JOIN Confirmations c2\n"
    "  ON c1.user_id = c2.user_id\n"
    " AND c1.time_stamp < c2.time_stamp\n"
    " AND TIMESTAMPDIFF(SECOND, c1.time_stamp, c2.time_stamp) <= 24 * 60 * 60\n";
