// LeetCode 1645 - Hopper Company Queries II
// https://leetcode.com/problems/hopper-company-queries-ii/

const char* QUERY =
    "\n"
    "WITH RECURSIVE months AS (\n"
    "  SELECT 1 AS month UNION ALL SELECT month + 1 FROM months WHERE month < 12\n"
    "), monthly AS (\n"
    "  SELECT m.month, COALESCE(SUM(ar.ride_distance), 0) AS distance,\n"
    "         COALESCE(SUM(ar.ride_duration), 0) AS duration\n"
    "  FROM months m\n"
    "  LEFT JOIN Rides r ON YEAR(r.requested_at) = 2020 AND MONTH(r.requested_at) = m.month\n"
    "  LEFT JOIN AcceptedRides ar ON ar.ride_id = r.ride_id\n"
    "  GROUP BY m.month\n"
    ")\n"
    "SELECT month,\n"
    "       ROUND((distance + LEAD(distance,1) OVER (ORDER BY month) + LEAD(distance,2) OVER (ORDER BY month)) / 3, 2) AS average_ride_distance,\n"
    "       ROUND((duration + LEAD(duration,1) OVER (ORDER BY month) + LEAD(duration,2) OVER (ORDER BY month)) / 3, 2) AS average_ride_duration\n"
    "FROM monthly\n"
    "ORDER BY month LIMIT 10;\n";
