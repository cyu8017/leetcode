// LeetCode 0586 - Customer Placing The Largest Number Of Orders
// https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

class Solution {
    companion object {
        const val QUERY = "SELECT customer_number\n" +
            "FROM Orders\n" +
            "GROUP BY customer_number\n" +
            "ORDER BY COUNT(*) DESC\n" +
            "LIMIT 1"
    }
}
