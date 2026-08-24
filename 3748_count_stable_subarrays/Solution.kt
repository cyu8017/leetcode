// LeetCode 3748 - Count Stable Subarrays
// https://leetcode.com/problems/count_stable_subarrays/

class Solution {
    fun countStableSubarrays(nums: IntArray, queries: Array<IntArray>): LongArray {
        var n = nums.size
        var seg = ArrayList<Int>()
        var s = ArrayList<Long>()
        s.add(0L)
        var l = 0
        for (r in 0 until n) {
            if (r == n - 1 || nums[r] > nums[r + 1]) {
                seg.add(l)
                var k = r - l + 1
                s.add(s[s.size - 1] + k * (k + 1) / 2)
                l = r + 1
            }
        }
        var ans = LongArray(queries.size)
        for (idx in 0 until queries.size) {
            var left = queries[idx][0]
            var right = queries[idx][1]
            var i = lowerBound(seg, left + 1)
            var j = lowerBound(seg, right + 1) - 1
            if (i > j) {
                var k = right - left + 1
                ans[idx] = k * (k + 1) / 2
            } else {
                var a = seg[i] - left
                var b = right - seg[j] + 1
                ans[idx] = a * (a + 1) / 2 + s[j] - s[i] + b * (b + 1) / 2
            }
        }
        return ans
    }

    private fun lowerBound(a: MutableList<Int>, x: Int): Int {
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
