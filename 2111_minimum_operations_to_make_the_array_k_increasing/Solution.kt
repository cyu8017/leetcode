// LeetCode 2111 - Minimum Operations to Make the Array K-Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/

class Solution {
    fun kIncreasing(arr: IntArray, k: Int): Int {
        var ans: Int = 0, n = arr.size
        for (start in 0 until k) {
            var seq = mutableListOf()
            run {
                var i = start
                while (i < n) {
                    seq.add(arr[i])
                    i += k
                }
            }
            var tails = mutableListOf()
            for (x in seq) {
                var lo: Int = 0, hi = tails.size
                while (lo < hi) {
                    var mid: Int = (lo + hi) / 2
                    if (tails.get(mid) <= x) lo = mid + 1
                    else hi = mid
                }
                if (lo == tails.size) tails.add(x)
                else tails.set(lo, x)
            }
            ans += seq.size - tails.size
        }
        return ans
    }
}
