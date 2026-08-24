// LeetCode 3415 - Find Products With Three Consecutive Digits
// https://leetcode.com/problems/find-products-with-three-consecutive-digits/

class Solution {
    companion object {
        const val QUERY = "SELECT product_id, name\n" +
            "FROM Products\n" +
            "WHERE name REGEXP '(^|[^0-9])[0-9]{3}([^0-9]|$)'\n" +
            "ORDER BY 1;"
    }
}
