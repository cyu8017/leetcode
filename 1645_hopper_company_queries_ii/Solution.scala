// LeetCode 1645 - Hopper Company Queries Ii
// https://leetcode.com/problems/hopper-company-queries-ii/

object Solution {
  final val QUERY: String = """WITH RECURSIVE months AS (
  SELECT 1 AS month UNION ALL SELECT month + 1 FROM months WHERE month < 12
), monthly AS (
  SELECT m.month, COALESCE(SUM(ar.ride_distance), 0) AS distance,
         COALESCE(SUM(ar.ride_duration), 0) AS duration
  FROM months m
  LEFT JOIN Rides r ON YEAR(r.requested_at) = 2020 AND MONTH(r.requested_at) = m.month
  LEFT JOIN AcceptedRides ar ON ar.ride_id = r.ride_id
  GROUP BY m.month
)
SELECT month,
       ROUND((distance + LEAD(distance,1) OVER (ORDER BY month) + LEAD(distance,2) OVER (ORDER BY month)) / 3, 2) AS average_ride_distance,
       ROUND((duration + LEAD(duration,1) OVER (ORDER BY month) + LEAD(duration,2) OVER (ORDER BY month)) / 3, 2) AS average_ride_duration
FROM monthly
ORDER BY month LIMIT 10;
"""
}
