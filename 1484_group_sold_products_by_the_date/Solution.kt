// LeetCode 1484 - Group Sold Products By The Date
// https://leetcode.com/problems/group-sold-products-by-the-date/

class Solution {
    companion object {
        const val QUERY = "SELECT sell_date, COUNT(DISTINCT product) AS num_sold,\n" +
            "       GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') AS products\n" +
            "FROM Activities GROUP BY sell_date ORDER BY sell_date"
    }
}
