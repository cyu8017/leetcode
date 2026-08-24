// LeetCode 0719 - Find K-th Smallest Pair Distance
// https://leetcode.com/problems/find-k-th-smallest-pair-distance/

class Solution {
    fun smallestDistancePair(nums: IntArray, k: Int): Int {
        nums.sort()
        var lo = 0
        var hi = nums[nums.size - 1] - nums[0]
        while (lo < hi) {
            var mid = lo + (hi - lo) / 2
            if (countPairs(nums, mid) >= k) hi = mid
            else lo = mid + 1
        }
        return lo
    }

    private fun countPairs(nums: IntArray, distance: Int): Int {
        var count = 0
        var left = 0
        for (right in 0 until nums.size) {
            while (nums[right] - nums[left] > distance) left++
            count += right - left
        }
        return count
    }
}
