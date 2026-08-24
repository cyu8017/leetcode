// LeetCode 1445 - Apples Oranges
// https://leetcode.com/problems/apples-oranges/

class Solution {
    companion object {
        const val QUERY = "SELECT sale_date,\n" +
            "       SUM(CASE WHEN fruit = 'apples' THEN sold_num ELSE -sold_num END) AS diff\n" +
            "FROM Sales\n" +
            "GROUP BY sale_date\n" +
            "ORDER BY sale_date"
    }
}
