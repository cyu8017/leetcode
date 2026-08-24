// LeetCode 2151 - Maximum Good People Based on Statements
// https://leetcode.com/problems/maximum-good-people-based-on-statements/

class Solution {
    fun ok(statements: Array<IntArray>, n: Int, mask: Int): Boolean {
        for (i in 0 until n) {
            if ((mask & (1 << i)) == 0) continue
            for (j in 0 until n) {
                var s: Int = statements[i][j]
                if (s == 2) continue
                var goodJ: Boolean = (mask & (1 << j)) != 0
                if ((s == 1 && !goodJ) || (s == 0 && goodJ)) return false
            }
        }
        return true
    }

    fun maximumGood(statements: Array<IntArray>): Int {
        var n: Int = statements.size, ans = 0
        for (mask in 0 until (1 << n))
            if (ok(statements, n, mask)) ans = maxOf(ans, Int.bitCount(mask))
        return ans
    }
}
