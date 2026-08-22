// LeetCode 0618 - Students Report By Geography
// https://leetcode.com/problems/students-report-by-geography/

const char* QUERY =
    "\n"
    "WITH ranked AS (\n"
    "    SELECT\n"
    "        name,\n"
    "        continent,\n"
    "        ROW_NUMBER() OVER (PARTITION BY continent ORDER BY name) AS rn\n"
    "    FROM Student\n"
    ")\n"
    "SELECT\n"
    "    MAX(CASE WHEN continent = 'America' THEN name END) AS America,\n"
    "    MAX(CASE WHEN continent = 'Asia' THEN name END) AS Asia,\n"
    "    MAX(CASE WHEN continent = 'Europe' THEN name END) AS Europe\n"
    "FROM ranked\n"
    "GROUP BY rn\n"
    "ORDER BY rn\n";
