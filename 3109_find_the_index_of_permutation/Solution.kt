// LeetCode 3109 - Find the Index of Permutation
// https://leetcode.com/problems/find-the-index-of-permutation/

class Solution {
    class BIT(private val n: Int) {
        private val c = IntArray(n + 1)
        fun update(x0: Int, delta: Int) {
            var x = x0
            while (x <= n) {
                c[x] += delta
                x += x and -x
            }
        }
        fun query(x0: Int): Int {
            var x = x0
            var s = 0
            while (x > 0) {
                s += c[x]
                x -= x and -x
            }
            return s
        }
    }

    fun getPermutationIndex(perm: IntArray): Int {
        val MOD = 1_000_000_007
        val n = perm.size
        val tree = BIT(n + 1)
        val f = IntArray(n)
        f[0] = 1
        for (i in 1 until n) f[i] = ((f[i - 1].toLong() * i) % MOD).toInt()
        var ans = 0L
        for (i in 0 until n) {
            val x = perm[i]
            val cnt = x - 1 - tree.query(x)
            ans = (ans + cnt.toLong() * f[n - 1 - i]) % MOD
            tree.update(x, 1)
        }
        return ans.toInt()
    }
}
