// LeetCode 2308 - Arrange Table by Gender
// https://leetcode.com/problems/arrange-table-by-gender/

const char* QUERY =
    "\n"
    "WITH\n"
    "    t AS (\n"
    "        SELECT\n"
    "            *,\n"
    "            RANK() OVER (\n"
    "                PARTITION BY gender\n"
    "                ORDER BY user_id\n"
    "            ) AS rk1,\n"
    "            CASE\n"
    "                WHEN gender = 'female' THEN 0\n"
    "                WHEN gender = 'other' THEN 1\n"
    "                ELSE 2\n"
    "            END AS rk2\n"
    "        FROM Genders\n"
    "    )\n"
    "SELECT user_id, gender\n"
    "FROM t\n"
    "ORDER BY rk1, rk2\n";
