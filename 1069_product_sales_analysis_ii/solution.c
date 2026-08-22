// LeetCode 1069 - Product Sales Analysis II
// https://leetcode.com/problems/product-sales-analysis-ii/

const char* QUERY =
    "\n"
    "SELECT product_id, SUM(quantity) AS total_quantity\n"
    "FROM Sales\n"
    "GROUP BY product_id\n";
