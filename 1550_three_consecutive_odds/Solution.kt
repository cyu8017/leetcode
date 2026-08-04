// LeetCode 1550 - Three Consecutive Odds
// https://leetcode.com/problems/three-consecutive-odds/

class Solution {
    fun threeConsecutiveOdds(arr: IntArray): Boolean {
        var run = 0
        for (value in arr) {
            if ((value and 1) == 1) {
                run++
                if (run == 3) return true
            } else {
                run = 0
            }
        }
        return false
    }
}
