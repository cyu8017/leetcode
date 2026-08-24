// LeetCode 3932 - Count K Th Roots In A Range
// https://leetcode.com/problems/count-k-th-roots-in-a-range/

class Solution {
    fun countKthRoots(l: Int, r: Int, k: Int): Int {
        if (k == 1) return r - l + 1
        var ans = 0
        var x = 0L
        while (true) {
            var y = 1L
            var tooBig = false
            for (i in 0 until k) {
                if (x != 0L && y > r.toLong() / x) {
                    tooBig = true
                    break
                }
                y *= x
                if (y > r) break
            }
            if (tooBig || y > r) break
            if (l <= y && y <= r) ans++
            x++
        }
        return ans
    }
}
