// LeetCode 1395 - Count Number of Teams
// https://leetcode.com/problems/count-number-of-teams/

class Solution {
    fun numTeams(rating: IntArray): Int {
        var ans = 0
        for (j in rating.indices) {
            val x = rating[j]
            var ll = 0
            var lg = 0
            for (i in 0 until j) {
                if (rating[i] < x) ll++ else lg++
            }
            var rg = 0
            var rl = 0
            for (i in j + 1 until rating.size) {
                if (rating[i] > x) rg++ else rl++
            }
            ans += ll * rg + lg * rl
        }
        return ans
    }
}
