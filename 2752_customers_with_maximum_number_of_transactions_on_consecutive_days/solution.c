// LeetCode 2752 - Customers with Maximum Number of Transactions on Consecutive Days
// https://leetcode.com/problems/customers-with-maximum-number-of-transactions-on-consecutive-days/

const char* QUERY =
    "\n"
    "WITH\n"
    "    s AS (\n"
    "        SELECT\n"
    "            customer_id,\n"
    "            DATE_SUB(\n"
    "                transaction_date,\n"
    "                INTERVAL ROW_NUMBER() OVER (\n"
    "                    PARTITION BY customer_id\n"
    "                    ORDER BY transaction_date\n"
    "                ) DAY\n"
    "            ) AS transaction_date\n"
    "        FROM Transactions\n"
    "    ),\n"
    "    t AS (\n"
    "        SELECT customer_id, transaction_date, COUNT(1) AS cnt\n"
    "        FROM s\n"
    "        GROUP BY 1, 2\n"
    "    )\n"
    "SELECT customer_id\n"
    "FROM t\n"
    "WHERE cnt = (SELECT MAX(cnt) FROM t)\n"
    "ORDER BY customer_id\n";
