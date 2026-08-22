// LeetCode 2388 - Change Null Values in a Table to the Previous Value
// https://leetcode.com/problems/change-null-values-in-a-table-to-the-previous-value/

const char* QUERY =
    "\n"
    "WITH\n"
    "    S AS (\n"
    "        SELECT *, ROW_NUMBER() OVER () AS rk\n"
    "        FROM CoffeeShop\n"
    "    ),\n"
    "    T AS (\n"
    "        SELECT\n"
    "            *,\n"
    "            SUM(\n"
    "                CASE\n"
    "                    WHEN drink IS NULL THEN 0\n"
    "                    ELSE 1\n"
    "                END\n"
    "            ) OVER (ORDER BY rk) AS gid\n"
    "        FROM S\n"
    "    )\n"
    "SELECT\n"
    "    id,\n"
    "    MAX(drink) OVER (\n"
    "        PARTITION BY gid\n"
    "        ORDER BY rk\n"
    "    ) AS drink\n"
    "FROM T\n";
