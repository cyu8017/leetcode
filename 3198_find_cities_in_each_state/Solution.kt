// LeetCode 3198 - Find Cities In Each State
// https://leetcode.com/problems/find-cities-in-each-state/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    state,\n" +
            "    GROUP_CONCAT(city ORDER BY city SEPARATOR ', ') cities\n" +
            "FROM cities\n" +
            "GROUP BY 1\n" +
            "ORDER BY 1;"
    }
}
