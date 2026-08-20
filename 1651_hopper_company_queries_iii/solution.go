// LeetCode 1651 - Hopper Company Queries III
// https://leetcode.com/problems/hopper-company-queries-iii/

const QUERY = `
WITH RECURSIVE months AS (
 SELECT 1 month UNION ALL SELECT month+1 FROM months WHERE month<12
), rides AS (
 SELECT MONTH(r.requested_at) month, SUM(a.ride_distance) distance, SUM(a.ride_duration) duration
 FROM Rides r JOIN AcceptedRides a USING(ride_id)
 WHERE YEAR(r.requested_at)=2020 GROUP BY MONTH(r.requested_at)
), totals AS (
 SELECT m.month, COALESCE(r.distance,0) distance, COALESCE(r.duration,0) duration
 FROM months m LEFT JOIN rides r USING(month)
)
SELECT month, ROUND(AVG(distance) OVER(ORDER BY month ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING),2) average_ride_distance,
ROUND(AVG(duration) OVER(ORDER BY month ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING),2) average_ride_duration
FROM totals ORDER BY month LIMIT 10
`
