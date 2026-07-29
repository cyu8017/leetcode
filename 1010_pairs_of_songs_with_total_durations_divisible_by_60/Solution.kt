// LeetCode 1010 - Pairs of Songs With Total Durations Divisible by 60
// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

class Solution {
    fun numPairsDivisibleBy60(time: IntArray): Int {
        val count = IntArray(60)
        var ans = 0
        for (t in time) {
            ans += count[(60 - t % 60) % 60]
            count[t % 60]++
        }
        return ans
    }
}
