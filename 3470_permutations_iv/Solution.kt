// LeetCode 3470 - Permutations IV
// https://leetcode.com/problems/permutations-iv/

class Solution {
    private var fact: LongArray? = null
    private var used: BooleanArray? = null
    private var ans: MutableList<Int>? = null
    private var k: Long = 0L
    private var n: Int = 0

    fun permute(n: Int, k: Long): IntArray {
        this.n = n
        this.k = k
        fact = LongArray(n + 1)
        fact[0] = 1
        for (i in 1 .. n) {
            fact[i] = fact[i - 1] * i
            if (fact[i] > 1e18) fact[i] = (long) 1e18 + 1
        }
        used = BooleanArray(n + 1)
        ans = ArrayList()
        if (!dfs(0)) return IntArray(0)
        var res = IntArray(ans.size)
        for (i in 0 until ans.size) { res[i] = ans[i] }
        return res
    }

    private fun dfs(pos: Int): Boolean {
        if (pos == n) return true
        for (x in 1 .. n) {
            if (used[x]) continue
            if (pos > 0 && (ans[pos - 1] % 2 == x % 2)) continue
            var rem = n - pos - 1
            var cnt = fact[rem]
            if (cnt >= k) {
                used[x] = true
                ans.add(x)
                if (dfs(pos + 1)) return true
                ans.remove(ans.size - 1)
                used[x] = false
            } else {
                k -= cnt
            }
        }
        return false
    }
}
