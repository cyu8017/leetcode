// LeetCode 1411 - Number of Ways to Paint N x 3 Grid
// https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/

class Solution {
    fun numOfWays(n: Int): Int {
        val mod = 1_000_000_007L
        var aba = 6L
        var abc = 6L
        for (i in 1 until n) {
            val nextAba = (3 * aba + 2 * abc) % mod
            val nextAbc = (2 * aba + 2 * abc) % mod
            aba = nextAba
            abc = nextAbc
        }
        return ((aba + abc) % mod).toInt()
    }
}
