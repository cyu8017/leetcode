// LeetCode 2320 - Count Number of Ways to Place Houses
// https://leetcode.com/problems/count-number-of-ways-to-place-houses/

class Solution {
    fun countHousePlacements(n: Int): Int {
        val mod = 1_000_000_007
        var a = 1L
        var b = 1L
        repeat(n) {
            val na = (a + b) % mod
            b = a
            a = na
        }
        val ways = (a + b) % mod
        return (ways * ways % mod).toInt()
    }
}
