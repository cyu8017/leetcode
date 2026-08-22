// LeetCode 2837 - Total Traveled Distance
// https://leetcode.com/problems/total-traveled-distance/

const char* QUERY =
    "\n"
    "SELECT u.user_id, u.name, IFNULL(SUM(r.distance), 0) AS `traveled distance`\n"
    "FROM Users AS u\n"
    "LEFT JOIN Rides AS r USING (user_id)\n"
    "GROUP BY u.user_id, u.name\n"
    "ORDER BY u.user_id\n";
