// LeetCode 1643 - Kth Smallest Instructions
// https://leetcode.com/problems/kth-smallest-instructions/

class Solution {
    fun kthSmallestPath(destination: IntArray, k: Int): String {
        var v = destination[0]
        var h = destination[1]
        var kk = k
        val ans = StringBuilder()
        while (h + v > 0) {
            if (h > 0) {
                val count = comb(h + v - 1, v)
                if (kk <= count) {
                    ans.append('H')
                    h--
                    continue
                }
                kk -= count
            }
            ans.append('V')
            v--
        }
        return ans.toString()
    }

    private fun comb(n: Int, r: Int): Int {
        if (r < 0 || r > n) return 0
        var num = 1L
        val rr = minOf(r, n - r)
        for (i in 0 until rr) {
            num = num * (n - i) / (i + 1)
        }
        return num.toInt()
    }
}
