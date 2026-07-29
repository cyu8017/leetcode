// LeetCode 1014 - Best Sightseeing Pair
// https://leetcode.com/problems/best-sightseeing-pair/

class Solution {
    fun maxScoreSightseeingPair(values: IntArray): Int {
        var best = values[0]; var ans = 0
        for (j in 1 until values.size) {
            ans = maxOf(ans, best + values[j] - j)
            best = maxOf(best, values[j] + j)
        }
        return ans
    }
}
