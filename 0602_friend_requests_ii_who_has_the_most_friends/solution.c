// LeetCode 0602 - Friend Requests II: Who Has the Most Friends
// https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/

const char* QUERY =
    "\n"
    "SELECT id, COUNT(*) AS num\n"
    "FROM (\n"
    "    SELECT requester_id AS id FROM RequestAccepted\n"
    "    UNION ALL\n"
    "    SELECT accepter_id AS id FROM RequestAccepted\n"
    ") friends\n"
    "GROUP BY id\n"
    "ORDER BY num DESC\n"
    "LIMIT 1\n";
