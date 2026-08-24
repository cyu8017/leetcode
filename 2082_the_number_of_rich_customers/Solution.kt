// LeetCode 2082 - The Number Of Rich Customers
// https://leetcode.com/problems/the-number-of-rich-customers/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    COUNT(DISTINCT customer_id) AS rich_count\n" +
            "FROM Store\n" +
            "WHERE amount > 500"
    }
}
