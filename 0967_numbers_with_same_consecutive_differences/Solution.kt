// LeetCode 0967 - Numbers With Same Consecutive Differences
// https://leetcode.com/problems/numbers-with-same-consecutive-differences/

class Solution {
    private val ans = mutableListOf<Int>()
    private var n = 0
    private var k = 0

    fun numsSameConsecDiff(n: Int, k: Int): IntArray {
        this.n = n
        this.k = k
        for (start in 1..9) dfs(start, 1)
        return ans.toIntArray()
    }

    private fun dfs(num: Int, length: Int) {
        if (length == n) {
            ans.add(num)
            return
        }
        val last = num % 10
        val nexts = hashSetOf(last + k, last - k)
        for (nxt in nexts) {
            if (nxt in 0..9) dfs(num * 10 + nxt, length + 1)
        }
    }
}
