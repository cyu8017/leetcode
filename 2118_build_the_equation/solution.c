// LeetCode 2118 - Build the Equation
// https://leetcode.com/problems/build-the-equation/

const char* QUERY =
    "\n"
    "WITH\n"
    "    T AS (\n"
    "        SELECT\n"
    "            power,\n"
    "            CASE power\n"
    "                WHEN 0 THEN IF(factor > 0, CONCAT('+', factor), factor)\n"
    "                WHEN 1 THEN CONCAT(\n"
    "                    IF(factor > 0, CONCAT('+', factor), factor),\n"
    "                    'X'\n"
    "                )\n"
    "                ELSE CONCAT(\n"
    "                    IF(factor > 0, CONCAT('+', factor), factor),\n"
    "                    'X^',\n"
    "                    power\n"
    "                )\n"
    "            END AS it\n"
    "        FROM Terms\n"
    "    )\n"
    "SELECT\n"
    "    CONCAT(GROUP_CONCAT(it ORDER BY power DESC SEPARATOR \"\"), '=0') AS equation\n"
    "FROM T\n";
