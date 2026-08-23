// LeetCode 2112 - The Airport With The Most Traffic
// https://leetcode.com/problems/the-airport-with-the-most-traffic/

var QUERY = `WITH
    T AS (
        SELECT * FROM Flights
        UNION
        SELECT arrival_airport, departure_airport, flights_count FROM Flights
    ),
    P AS (
        SELECT departure_airport, SUM(flights_count) AS cnt
        FROM T
        GROUP BY 1
    )
SELECT departure_airport AS airport_id
FROM P
WHERE cnt = (SELECT MAX(cnt) FROM P)`;

module.exports = { QUERY };
