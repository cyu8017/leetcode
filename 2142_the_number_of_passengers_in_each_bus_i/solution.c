// LeetCode 2142 - The Number of Passengers in Each Bus I
// https://leetcode.com/problems/the-number-of-passengers-in-each-bus-i/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    bus_id,\n"
    "    COUNT(passenger_id) - LAG(COUNT(passenger_id), 1, 0) OVER (\n"
    "        ORDER BY MIN(b.arrival_time)\n"
    "    ) AS passengers_cnt\n"
    "FROM Buses AS b\n"
    "LEFT JOIN Passengers AS p ON p.arrival_time <= b.arrival_time\n"
    "GROUP BY bus_id\n"
    "ORDER BY bus_id\n";
