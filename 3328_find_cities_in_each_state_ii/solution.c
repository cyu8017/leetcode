// LeetCode 3328 - Find Cities in Each State II
// https://leetcode.com/problems/find-cities-in-each-state-ii/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    state,\n"
    "    GROUP_CONCAT(city ORDER BY city SEPARATOR ', ') AS cities,\n"
    "    COUNT(\n"
    "        CASE\n"
    "            WHEN LEFT(city, 1) = LEFT(state, 1) THEN 1\n"
    "        END\n"
    "    ) AS matching_letter_count\n"
    "FROM cities\n"
    "GROUP BY 1\n"
    "HAVING COUNT(city) >= 3 AND matching_letter_count > 0\n"
    "ORDER BY 3 DESC, 1;\n";
