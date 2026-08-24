// LeetCode 0689 - Maximum Sum of 3 Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

class Solution {
    fun maxSumOfThreeSubarrays(nums: IntArray, k: Int): IntArray {
        var n = nums.size
        var windows = n - k + 1
        var sums = IntArray(windows)
        var total = 0
        for (i in 0 until k) { total += nums[i] }
        sums[0] = total
        for (i in 1 until windows) {
            total += nums[i + k - 1] - nums[i - 1]
            sums[i] = total
        }
        var left = IntArray(windows)
        var best = 0
        for (i in 0 until windows) {
            if (sums[i] > sums[best]) best = i
            left[i] = best
        }
        var right = IntArray(windows)
        best = windows - 1
        for (i in windows - 1 downTo 0) {
            if (sums[i] >= sums[best]) best = i
            right[i] = best
        }
        var answer = {0, 0, 0}
        var bestTotal = -1
        for (mid in k until windows - k) {
            var l = left[mid - k]
            var r = right[mid + k]
            var cur = sums[l] + sums[mid] + sums[r]
            if (cur > bestTotal) {
                bestTotal = cur
                answer = intArrayOf(l, mid, r)
            }
        }
        return answer
    }
}
