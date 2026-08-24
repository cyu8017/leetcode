// LeetCode 1821 - Find Customers With Positive Revenue This Year
// https://leetcode.com/problems/find-customers-with-positive-revenue-this-year/

class Solution {
    companion object {
        const val QUERY = "SELECT customer_id\n" +
            "FROM Customers\n" +
            "WHERE year = 2021 AND revenue > 0"
    }
}
