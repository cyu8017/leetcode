// LeetCode 3522 - Calculate Score After Performing Instructions
// https://leetcode.com/problems/calculate-score-after-performing-instructions/

class Solution {
    fun calculateScore(instructions: Array<String>, values: IntArray): Long {
        var n = values.size
        var vis = BooleanArray(n)
        var ans = 0
        var i = 0
        while (i >= 0 && i < n && !vis[i]) {
            vis[i] = true
            if (instructions[i][0] == 'a') {
                ans += values[i]
                i += 1
            } else {
                i += values[i]
            }
        }
        return ans
    }
}
