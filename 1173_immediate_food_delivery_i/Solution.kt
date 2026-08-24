// LeetCode 1173 - Immediate Food Delivery I
// https://leetcode.com/problems/immediate-food-delivery-i/

class Solution {
    companion object {
        const val QUERY = "SELECT ROUND(\n" +
            "    100.0 * SUM(order_date = customer_pref_delivery_date) / COUNT(*),\n" +
            "    2\n" +
            ") AS immediate_percentage\n" +
            "FROM Delivery"
    }
}
