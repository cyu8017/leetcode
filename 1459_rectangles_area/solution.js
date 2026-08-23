// LeetCode 1459 - Rectangles Area
// https://leetcode.com/problems/rectangles-area/

var QUERY = `SELECT p1.id AS P1, p2.id AS P2,
       ABS(p1.x_value - p2.x_value) * ABS(p1.y_value - p2.y_value) AS AREA
FROM Points p1
JOIN Points p2 ON p1.id < p2.id
WHERE p1.x_value <> p2.x_value AND p1.y_value <> p2.y_value
ORDER BY AREA DESC, P1, P2`;

module.exports = { QUERY };
