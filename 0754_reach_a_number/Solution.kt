// LeetCode 0754 - Reach a Number
// https://leetcode.com/problems/reach-a-number/

class Solution {
    fun reachNumber(target: Int): Int {
        var target = target
        target = kotlin.math.abs(target)
        var steps = 0
        var total = 0
        while (total < target || (total - target) % 2 != 0) {
            steps++
            total += steps
        }
        return steps
    }
}
