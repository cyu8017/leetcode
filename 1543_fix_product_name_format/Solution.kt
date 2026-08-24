// LeetCode 1543 - Fix Product Name Format
// https://leetcode.com/problems/fix-product-name-format/

class Solution {
    companion object {
        const val QUERY = "SELECT LOWER(TRIM(product_name)) AS product_name,\n" +
            "       DATE_FORMAT(sale_date, '%Y-%m') AS sale_date,\n" +
            "       COUNT(*) AS total\n" +
            "FROM Sales\n" +
            "GROUP BY LOWER(TRIM(product_name)), DATE_FORMAT(sale_date, '%Y-%m')\n" +
            "ORDER BY product_name, sale_date"
    }
}
