// LeetCode 0262 - Trips and Users
// https://leetcode.com/problems/trips-and-users/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    Request_at AS Day,\n"
    "    ROUND(\n"
    "        SUM(CASE WHEN Status <> 'completed' THEN 1 ELSE 0 END) / COUNT(*),\n"
    "        2\n"
    "    ) AS `Cancellation Rate`\n"
    "FROM Trips\n"
    "INNER JOIN Users ON Trips.Client_Id = Users.Users_Id AND Users.Role = 'client'\n"
    "WHERE Users.Banned = 'No'\n"
    "    AND Request_at BETWEEN '2013-10-01' AND '2013-10-03'\n"
    "GROUP BY Request_at\n"
    "ORDER BY Day\n";
