// LeetCode 3825 - Longest Strictly Increasing Subsequence With Non Zero Bitwise And
// https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/

class Solution {
    private fun bitLen(x: Int): Int {
        if (x == 0) return 0
        var n = 0
        while (x > 0) { n++; x >>= 1; }
        return n
    }

    private fun lis(arr: MutableList<Int>): Int {
        var g = ArrayList<Int>()
        for (x in arr) {
            var idx = Collections.binarySearch(g, x)
            if (idx < 0) idx = ~idx
            if (idx == g.size) g.add(x)
            else g.set(idx, x)
        }
        return g.size
    }

    fun longestSubsequence(nums: IntArray): Int {
        var ans = 0
        var mx = 0
        for (x in nums) { mx = maxOf(mx, x) }
        var m = bitLen(mx)
        for (i in 0 until m) {
            var arr = ArrayList<Int>()
            for (x in nums) {
                if (((x  shr  i) & 1) != 0) arr.add(x)
            }
            ans = maxOf(ans, lis(arr))
        }
        return ans
    }
}
