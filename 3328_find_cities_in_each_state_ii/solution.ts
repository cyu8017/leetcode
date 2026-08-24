// LeetCode 3328 - Find Cities In Each State Ii
// https://leetcode.com/problems/find-cities-in-each-state-ii/

export const QUERY = `SELECT
    state,
    GROUP_CONCAT(city ORDER BY city SEPARATOR ', ') AS cities,
    COUNT(
        CASE
            WHEN LEFT(city, 1) = LEFT(state, 1) THEN 1
        END
    ) AS matching_letter_count
FROM cities
GROUP BY 1
HAVING COUNT(city) >= 3 AND matching_letter_count > 0
ORDER BY 3 DESC, 1;`;
