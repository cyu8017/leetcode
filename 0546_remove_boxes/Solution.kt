// LeetCode 0546 - Remove Boxes
// https://leetcode.com/problems/remove-boxes/

class Solution {
    private lateinit var boxes: IntArray
    private lateinit var memo: Array<Array<IntArray>>

    fun removeBoxes(boxes: IntArray): Int {
        this.boxes = boxes
        val n = boxes.size
        memo = Array(n) { Array(n) { IntArray(n) { -1 } } }
        return dp(0, n - 1, 0)
    }

    private fun dp(left: Int, right: Int, streak: Int): Int {
        if (left > right) {
            return 0
        }
        if (memo[left][right][streak] != -1) {
            return memo[left][right][streak]
        }

        var r = right
        var s = streak
        while (r > left && boxes[r] == boxes[r - 1]) {
            r--
            s++
        }

        var best = (s + 1) * (s + 1) + dp(left, r - 1, 0)
        for (i in left until r) {
            if (boxes[i] == boxes[r]) {
                best = maxOf(best, dp(left, i, s + 1) + dp(i + 1, r - 1, 0))
            }
        }

        memo[left][right][streak] = best
        return best
    }
}
