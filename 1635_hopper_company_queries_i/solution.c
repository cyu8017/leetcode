// LeetCode 1635 - Hopper Company Queries I
// https://leetcode.com/problems/hopper-company-queries-i/

const char* QUERY =
    "\n"
    "WITH RECURSIVE months AS (\n"
    "  SELECT 1 AS month UNION ALL SELECT month + 1 FROM months WHERE month < 12\n"
    ")\n"
    "SELECT m.month,\n"
    "       (SELECT COUNT(*) FROM Drivers d WHERE d.join_date < DATE_ADD('2020-01-01', INTERVAL m.month MONTH)) AS active_drivers,\n"
    "       COUNT(ar.ride_id) AS accepted_rides\n"
    "FROM months m\n"
    "LEFT JOIN Rides r ON YEAR(r.requested_at) = 2020 AND MONTH(r.requested_at) = m.month\n"
    "LEFT JOIN AcceptedRides ar ON ar.ride_id = r.ride_id\n"
    "GROUP BY m.month ORDER BY m.month;\n";
