// LeetCode 1128 - Number of Equivalent Domino Pairs
// https://leetcode.com/problems/number-of-equivalent-domino-pairs/

class Solution {
    fun numEquivDominoPairs(dominoes: Array<IntArray>): Int {
        val count = mutableMapOf<Int, Int>()
        var ans = 0
        for (d in dominoes) {
            val a = minOf(d[0], d[1])
            val b = maxOf(d[0], d[1])
            val key = a * 10 + b
            val c = count.getOrDefault(key, 0)
            ans += c
            count[key] = c + 1
        }
        return ans
    }
}
