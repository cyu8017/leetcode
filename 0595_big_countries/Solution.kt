// LeetCode 0595 - Big Countries
// https://leetcode.com/problems/big-countries/

class Solution {
    companion object {
        const val QUERY = "SELECT name, population, area\n" +
            "FROM World\n" +
            "WHERE area >= 3000000 OR population >= 25000000"
    }
}
