// LeetCode 1251 - Average Selling Price
// https://leetcode.com/problems/average-selling-price/

class Solution {
    companion object {
        const val QUERY = "SELECT p.product_id,\n" +
            "       ROUND(SUM(p.price * u.units) / SUM(u.units), 2) AS average_price\n" +
            "FROM Prices p\n" +
            "JOIN UnitsSold u\n" +
            "  ON p.product_id = u.product_id\n" +
            " AND u.purchase_date BETWEEN p.start_date AND p.end_date\n" +
            "GROUP BY p.product_id"
    }
}
