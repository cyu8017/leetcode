// LeetCode 3198 - Find Cities in Each State
// https://leetcode.com/problems/find-cities-in-each-state/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    state,\n"
    "    GROUP_CONCAT(city ORDER BY city SEPARATOR ', ') cities\n"
    "FROM cities\n"
    "GROUP BY 1\n"
    "ORDER BY 1;\n";
