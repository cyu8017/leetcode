// LeetCode 1578 - Minimum Time to Make Rope Colorful
// https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

class Solution {
    fun minCost(colors: String, neededTime: IntArray): Int {
        var answer = 0
        var maximum = 0
        for (i in neededTime.indices) {
            if (i > 0 && colors[i] != colors[i - 1]) maximum = 0
            answer += minOf(maximum, neededTime[i])
            maximum = maxOf(maximum, neededTime[i])
        }
        return answer
    }
}
