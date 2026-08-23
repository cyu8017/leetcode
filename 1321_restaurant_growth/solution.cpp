// LeetCode 1321 - Restaurant Growth
// https://leetcode.com/problems/restaurant-growth/

const char* QUERY = R"SQL(
WITH daily AS (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
)
SELECT visited_on,
       SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
       ROUND(AVG(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount
FROM daily
ORDER BY visited_on
LIMIT 18446744073709551615 OFFSET 6
)SQL";
