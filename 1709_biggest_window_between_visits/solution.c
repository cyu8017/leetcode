// LeetCode 1709 - Biggest Window Between Visits
// https://leetcode.com/problems/biggest-window-between-visits/

const char* QUERY =
    "\n"
    "SELECT user_id, MAX(DATEDIFF(next_visit, visit_date)) AS biggest_window\n"
    "FROM (\n"
    "    SELECT\n"
    "        user_id,\n"
    "        visit_date,\n"
    "        LEAD(visit_date, 1, '2021-1-1') OVER (\n"
    "            PARTITION BY user_id\n"
    "            ORDER BY visit_date\n"
    "        ) AS next_visit\n"
    "    FROM UserVisits\n"
    ") AS visits\n"
    "GROUP BY user_id\n"
    "ORDER BY user_id;\n";
