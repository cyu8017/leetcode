// LeetCode 1436 - Destination City
// https://leetcode.com/problems/destination-city/

class Solution {
    fun destCity(paths: List<List<String>>): String {
        val starts = paths.map { it[0] }.toSet()
        return paths.first { it[1] !in starts }[1]
    }
}
