// LeetCode 1753 - Maximum Score From Removing Stones
// https://leetcode.com/problems/maximum-score-from-removing-stones/

class Solution {
    fun maximumScore(a: Int, b: Int, c: Int): Int {
        val stones = intArrayOf(a, b, c)
        stones.sortDescending()
        var score = 0
        while (stones[0] > 0 && stones[1] > 0) {
            stones[0]--
            stones[1]--
            score++
            stones.sortDescending()
        }
        return score
    }
}
