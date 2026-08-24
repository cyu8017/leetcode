// LeetCode 3465 - Find Products With Valid Serial Numbers
// https://leetcode.com/problems/find-products-with-valid-serial-numbers/

class Solution {
    companion object {
        const val QUERY = "SELECT product_id, product_name, description\n" +
            "FROM products\n" +
            "WHERE description REGEXP '(?-i)\\\\bSN[0-9]{4}-[0-9]{4}\\\\b'\n" +
            "ORDER BY 1;"
    }
}
