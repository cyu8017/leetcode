// LeetCode 2992 - Number of Self-Divisible Permutations
// https://leetcode.com/problems/number-of-self-divisible-permutations/

class Solution {
    private var ans = 0
    private lateinit var used: BooleanArray
    private var n = 0

    private fun gcd(a0: Int, b0: Int): Int {
        var a = a0; var b = b0
        while (b != 0) { val t = a % b; a = b; b = t }
        return a
    }

    private fun dfs(pos: Int) {
        if (pos > n) { ans++; return }
        for (v in 1..n) {
            if (used[v]) continue
            if (gcd(v, pos) != 1) continue
            used[v] = true
            dfs(pos + 1)
            used[v] = false
        }
    }

    fun selfDivisiblePermutationCount(n: Int): Int {
        this.n = n; ans = 0; used = BooleanArray(n + 1); dfs(1); return ans
    }
}
