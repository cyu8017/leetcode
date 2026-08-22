// LeetCode 2993 - Friday Purchases I
// https://leetcode.com/problems/friday-purchases-i/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    CEIL(DAYOFMONTH(purchase_date) / 7) AS week_of_month,\n"
    "    purchase_date,\n"
    "    SUM(amount_spend) AS total_amount\n"
    "FROM Purchases\n"
    "WHERE DATE_FORMAT(purchase_date, '%Y%m') = '202311' AND DAYOFWEEK(purchase_date) = 6\n"
    "GROUP BY 2\n"
    "ORDER BY 1\n";
