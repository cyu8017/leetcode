// LeetCode 2838 - Maximum Coins Heroes Can Collect
// https://leetcode.com/problems/maximum-coins-heroes-can-collect/


class Solution {
    fun maximumCoins(heroes: IntArray, monsters: IntArray, coins: IntArray): LongArray {
        val n = monsters.size
        val idx = Array(n) { it }
        idx.sortBy { monsters[it] }
        val pref = LongArray(n + 1)
        val ms = IntArray(n)
        for (i in 0 until n) {
            ms[i] = monsters[idx[i]]
            pref[i + 1] = pref[i] + coins[idx[i]]
        }
        val ans = LongArray(heroes.size)
        for (i in heroes.indices) {
            ans[i] = pref[upperBound(ms, heroes[i])]
        }
        return ans
    }

    private fun upperBound(a: IntArray, x: Int): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            val mid = (lo + hi) ushr 1
            if (a[mid] <= x) lo = mid + 1 else hi = mid
        }
        return lo
    }
}
