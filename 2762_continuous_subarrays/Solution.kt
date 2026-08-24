// LeetCode 2762 - Continuous Subarrays
// https://leetcode.com/problems/continuous-subarrays/

class Solution {
    fun continuousSubarrays(nums: IntArray): Long {
        var ans = 0
        var left = 0
        var freq = TreeMap<Int, Int>()
        for (right in 0 until nums.size) {
            freq[nums[right]] = freq.getOrDefault(nums[right], 0 + 1)
            while (freq.lastKey() - freq.firstKey() > 2) {
                var v = nums[left++]
                var c = freq[v] - 1
                if (c == 0) freq.remove(v)
                else freq[v] = c
            }
            ans += right - left + 1
        }
        return ans
    }
}
