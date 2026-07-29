// LeetCode 1088 - Confusing Number II
// https://leetcode.com/problems/confusing-number-ii/

class Solution {
    private var ans = 0
    private var n = 0
    private val rotate = intArrayOf(0, 1, -1, -1, -1, -1, 9, -1, 8, 6)
    private val digits = intArrayOf(0, 1, 6, 8, 9)

    fun confusingNumberII(n: Int): Int {
        this.n = n
        this.ans = 0
        dfs(0)
        return ans
    }

    private fun isConfusing(num: Int): Boolean {
        var x = num
        var rotated = 0
        while (x > 0) {
            val d = x % 10
            rotated = rotated * 10 + rotate[d]
            x /= 10
        }
        return rotated != num
    }

    private fun dfs(cur: Long) {
        if (cur > n) return
        if (cur != 0L && isConfusing(cur.toInt())) ans++
        if (cur == 0L) {
            for (d in intArrayOf(1, 6, 8, 9)) dfs(d.toLong())
        } else {
            for (d in digits) dfs(cur * 10 + d)
        }
    }
}
