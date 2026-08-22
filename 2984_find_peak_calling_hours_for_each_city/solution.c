// LeetCode 2984 - Find Peak Calling Hours for Each City
// https://leetcode.com/problems/find-peak-calling-hours-for-each-city/

const char* QUERY =
    "\n"
    "WITH\n"
    "    T AS (\n"
    "        SELECT\n"
    "            *,\n"
    "            RANK() OVER (\n"
    "                PARTITION BY city\n"
    "                ORDER BY cnt DESC\n"
    "            ) AS rk\n"
    "        FROM\n"
    "            (\n"
    "                SELECT\n"
    "                    city,\n"
    "                    HOUR(call_time) AS h,\n"
    "                    COUNT(1) AS cnt\n"
    "                FROM Calls\n"
    "                GROUP BY 1, 2\n"
    "            ) AS t\n"
    "    )\n"
    "SELECT city, h AS peak_calling_hour, cnt AS number_of_calls\n"
    "FROM T\n"
    "WHERE rk = 1\n"
    "ORDER BY 2 DESC, 1 DESC\n";
