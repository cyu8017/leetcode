// LeetCode 2561 - Rearranging Fruits
// https://leetcode.com/problems/rearranging-fruits/

class Solution {
    fun minCost(basket1: IntArray, basket2: IntArray): Long {
        val freq = HashMap<Int, Int>()
        var mn = Int.MAX_VALUE
        for (x in basket1) {
            freq[x] = freq.getOrDefault(x, 0) + 1
            mn = minOf(mn, x)
        }
        for (x in basket2) {
            freq[x] = freq.getOrDefault(x, 0) - 1
            mn = minOf(mn, x)
        }
        val extra = ArrayList<Int>()
        for ((key, value) in freq) {
            if (value % 2 != 0) return -1
            repeat(kotlin.math.abs(value) / 2) { extra.add(key) }
        }
        extra.sort()
        var ans = 0L
        for (i in 0 until extra.size / 2) {
            ans += minOf(extra[i].toLong(), 2L * mn)
        }
        return ans
    }
}
