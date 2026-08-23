// LeetCode 2118 - Build The Equation
// https://leetcode.com/problems/build-the-equation/

var QUERY = `WITH
    T AS (
        SELECT
            power,
            CASE power
                WHEN 0 THEN IF(factor > 0, CONCAT('+', factor), factor)
                WHEN 1 THEN CONCAT(
                    IF(factor > 0, CONCAT('+', factor), factor),
                    'X'
                )
                ELSE CONCAT(
                    IF(factor > 0, CONCAT('+', factor), factor),
                    'X^',
                    power
                )
            END AS it
        FROM Terms
    )
SELECT
    CONCAT(GROUP_CONCAT(it ORDER BY power DESC SEPARATOR ""), '=0') AS equation
FROM T`;

module.exports = { QUERY };
