// LeetCode 1769 - Minimum Number of Operations to Move All Balls to Each Box
// https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution {
    fun minOperations(boxes: String): IntArray {
        val n = boxes.length
        val ans = IntArray(n)
        var balls = 0
        var ops = 0
        for (i in 1 until n) {
            balls += boxes[i - 1] - '0'
            ops += balls
            ans[i] = ops
        }
        balls = 0
        ops = 0
        for (i in n - 2 downTo 0) {
            balls += boxes[i + 1] - '0'
            ops += balls
            ans[i] += ops
        }
        return ans
    }
}
