// LeetCode 3911 - K-th Smallest Remaining Even Integer in Subarray Queries
// https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/

class Solution {
    fun kthSmallestEven(nums: IntArray, queries: Array<IntArray>): LongArray {
        var n = nums.size
        var evenPrefix = IntArray(n + 1)
        for (i in 0 until n) {
            evenPrefix[i + 1] = evenPrefix[i] + (nums[i] % 2 == 0 ? 1 : 0)
        }
        var ans = LongArray(queries.size)
        for (qi in 0 until queries.size) {
            var l = queries[qi][0]
            var r = queries[qi][1]
            var k = queries[qi][2]
            var lo = 1
            var hi = k + (r - l + 1)
            while (lo < hi) {
                var mid = (lo + hi) / 2
                var pos = UpperBound(nums, 2 * mid)
                if (pos > r + 1) pos = r + 1
                var removed = 0
                if (pos > l) removed = evenPrefix[pos] - evenPrefix[l]
                if (mid - removed >= k) hi = mid
                else lo = mid + 1
            }
            ans[qi] = 2 * lo
        }
        return ans
    }
    fun UpperBound(a: IntArray, x: Long): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            var mid = (lo + hi) / 2
            if (a[mid] <= x) lo = mid + 1
            else hi = mid
        }
        return lo
    }
}
