// LeetCode 1651 - Hopper Company Queries III
// https://leetcode.com/problems/hopper-company-queries-iii/

const char* QUERY =
    "\n"
    "WITH RECURSIVE months AS (\n"
    " SELECT 1 month UNION ALL SELECT month+1 FROM months WHERE month<12\n"
    "), rides AS (\n"
    " SELECT MONTH(r.requested_at) month, SUM(a.ride_distance) distance, SUM(a.ride_duration) duration\n"
    " FROM Rides r JOIN AcceptedRides a USING(ride_id)\n"
    " WHERE YEAR(r.requested_at)=2020 GROUP BY MONTH(r.requested_at)\n"
    "), totals AS (\n"
    " SELECT m.month, COALESCE(r.distance,0) distance, COALESCE(r.duration,0) duration\n"
    " FROM months m LEFT JOIN rides r USING(month)\n"
    ")\n"
    "SELECT month, ROUND(AVG(distance) OVER(ORDER BY month ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING),2) average_ride_distance,\n"
    "ROUND(AVG(duration) OVER(ORDER BY month ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING),2) average_ride_duration\n"
    "FROM totals ORDER BY month LIMIT 10\n";
