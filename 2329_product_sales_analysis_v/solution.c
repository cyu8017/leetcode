// LeetCode 2329 - Product Sales Analysis V
// https://leetcode.com/problems/product-sales-analysis-v/

const char* QUERY =
    "\n"
    "SELECT user_id, SUM(quantity * price) AS spending\n"
    "FROM\n"
    "    Sales\n"
    "    JOIN Product USING (product_id)\n"
    "GROUP BY 1\n"
    "ORDER BY 2 DESC, 1\n";
