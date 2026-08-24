// LeetCode 2602 - Minimum Operations to Make All Array Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

class Solution {
    fun minOperations(nums: IntArray, queries: IntArray): LongArray {
        nums.sort()
        var n = nums.size
        var pref = LongArray(n + 1)
        for (i in 0 until n) { pref[i + 1] = pref[i] + nums[i] }
        var ans = LongArray(queries.size)
        for (qi in 0 until queries.size) {
            var q = queries[qi]
            var i = LowerBound(nums, q)
            var left = q * i - pref[i]
            var right = pref[n] - pref[i] - q * (n - i)
            ans[qi] = left + right
        }
        return ans
    }

    fun LowerBound(a: IntArray, x: Int): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            var mid = (lo + hi) / 2
            if (a[mid] < x) lo = mid + 1
            else hi = mid
        }
        return lo
    }
}
