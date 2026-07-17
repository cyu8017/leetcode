// LeetCode 1711 - Count Good Meals
// https://leetcode.com/problems/count-good-meals/

class Solution {
    fun countPairs(deliciousness: IntArray): Int {
        val mod = 1_000_000_007L
        val seen = HashMap<Int, Long>()
        var ans = 0L
        for (value in deliciousness) {
            for (power in 0 until 22) {
                seen[(1 shl power) - value]?.let { ans += it }
            }
            seen[value] = (seen[value] ?: 0L) + 1L
        }
        return (ans % mod).toInt()
    }
}
