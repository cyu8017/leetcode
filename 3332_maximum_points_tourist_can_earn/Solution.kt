// LeetCode 3332 - Maximum Points Tourist Can Earn
// https://leetcode.com/problems/maximum-points-tourist-can-earn/

class Solution {
    fun maxScore(n: Int, k: Int, stayScore: Array<IntArray>, travelScore: Array<IntArray>): Int {
        var dp = IntArray(n)
        for (day in 0 until k) {
            var ndp = IntArray(n)
            for (i in 0 until n) { ndp[i] = -(1  shl  30) }
            for (dest in 0 until n) {
                var best = -(1  shl  30)
                for (src in 0 until n) {
                    var `val` = dp[src]
                    if (src == dest) val += stayScore[day][dest]
                    else val += travelScore[src][dest]
                    if (val > best) best = val
                }
                ndp[dest] = best
            }
            dp = ndp
        }
        var ans = dp[0]
        for (i in 1 until n) { if (dp[i] > ans) ans = dp[i] }
        return ans
    }
}
