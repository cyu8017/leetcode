// LeetCode 2238 - Number Of Times A Driver Was A Passenger
// https://leetcode.com/problems/number-of-times-a-driver-was-a-passenger/

var QUERY = `WITH T AS (SELECT DISTINCT driver_id FROM Rides)
SELECT t.driver_id, COUNT(passenger_id) AS cnt
FROM
    T AS t
    LEFT JOIN Rides AS r ON t.driver_id = r.passenger_id
GROUP BY 1`;

module.exports = { QUERY };
