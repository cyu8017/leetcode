// LeetCode 2991 - Top Three Wineries
// https://leetcode.com/problems/top-three-wineries/

const char* QUERY =
    "\n"
    "WITH\n"
    "    T AS (\n"
    "        SELECT\n"
    "            country,\n"
    "            CONCAT(winery, ' (', points, ')') AS winery,\n"
    "            RANK() OVER (\n"
    "                PARTITION BY country\n"
    "                ORDER BY points DESC, winery\n"
    "            ) AS rk\n"
    "        FROM (SELECT country, SUM(points) AS points, winery FROM Wineries GROUP BY 1, 3) AS t\n"
    "    )\n"
    "SELECT\n"
    "    t1.country,\n"
    "    t1.winery AS top_winery,\n"
    "    IFNULL(t2.winery, 'No second winery') AS second_winery,\n"
    "    IFNULL(t3.winery, 'No third winery') AS third_winery\n"
    "FROM\n"
    "    T AS t1\n"
    "    LEFT JOIN T AS t2 ON t1.country = t2.country AND t1.rk = t2.rk - 1\n"
    "    LEFT JOIN T AS t3 ON t2.country = t3.country AND t2.rk = t3.rk - 1\n"
    "WHERE t1.rk = 1\n"
    "ORDER BY 1\n";
