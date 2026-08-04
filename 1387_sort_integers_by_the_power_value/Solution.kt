// LeetCode 1387 - Sort Integers by The Power Value
// https://leetcode.com/problems/sort-integers-by-the-power-value/

class Solution {
    private val memo = mutableMapOf<Int, Int>()

    fun getKth(lo: Int, hi: Int, k: Int): Int {
        return (lo..hi).sortedWith(compareBy({ power(it) }, { it }))[k - 1]
    }

    private fun power(x: Int): Int {
        memo[x]?.let { return it }
        val res = if (x == 1) 0 else 1 + power(if (x % 2 == 0) x / 2 else 3 * x + 1)
        memo[x] = res
        return res
    }
}
