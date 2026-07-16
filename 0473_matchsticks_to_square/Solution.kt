// LeetCode 0473 - Matchsticks to Square
// https://leetcode.com/problems/matchsticks-to-square/

class Solution {
    fun makesquare(matchsticks: IntArray): Boolean {
        if (matchsticks.isEmpty()) {
            return false
        }
        val total = matchsticks.sum()
        if (total % 4 != 0) {
            return false
        }
        val side = total / 4
        val sticks = matchsticks.sortedDescending().toIntArray()
        return dfs(0, sticks, IntArray(4), side)
    }

    private fun dfs(index: Int, matchsticks: IntArray, sides: IntArray, side: Int): Boolean {
        if (index == matchsticks.size) {
            return sides.all { it == side }
        }
        val length = matchsticks[index]
        for (sideIndex in 0 until 4) {
            if (sides[sideIndex] + length > side) {
                continue
            }
            if (sideIndex > 0 && sides[sideIndex] == sides[sideIndex - 1]) {
                continue
            }
            sides[sideIndex] += length
            if (dfs(index + 1, matchsticks, sides, side)) {
                return true
            }
            sides[sideIndex] -= length
        }
        return false
    }
}
