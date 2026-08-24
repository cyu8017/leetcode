// LeetCode 3337 - Total Characters in String After Transformations II
// https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

class Solution {
    private fun matMul(a: Array<IntArray>, b: Array<IntArray>, mod: Int): Array<IntArray> {
        var n = a.size
        var c = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            for (k in 0 until n) {
                if (a[i][k] == 0) continue
                for (j in 0 until n) {
                    c[i][j] = (c[i][j] + (a[i][k] * b[k][j] % mod)) % mod
                }
            }
        }
        return c
    }

    private fun matPow(a: Array<IntArray>, e: Int, mod: Int): Array<IntArray> {
        var n = a.size
        var r = Array(n) { IntArray(n) }
        for (i in 0 until n) { r[i][i] = 1 }
        while (e > 0) {
            if ((e and 1) != 0) r = matMul(r, a, mod)
            a = matMul(a, a, mod)
            e = e shr 1
        }
        return r
    }

    fun lengthAfterTransformations(s: String, t: Int, nums: MutableList<Int>): Int {
        val mod = 1_000_000_007
        var mat = Array(26) { IntArray(26) }
        for (i in 0 until 26) {
            for (j in 1 ..nums[i]) { mat[i][(i + j) % 26] = 1 }
        }
        mat = matPow(mat, t, mod)
        var cnt = IntArray(26)
        for (c in s.toCharArray()) { cnt[c - 'a'] = cnt[c - 'a'] + 1 }
        var ans = 0
        for (i in 0 until 26) {
            for (j in 0 until 26) {
                ans = (ans + (cnt[i] * mat[i][j] % mod)) % mod
            }
        }
        return ans
    }
}
