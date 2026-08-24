// LeetCode 2841 - Maximum Sum of Almost Unique Subarray
// https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

class Solution {
    fun maxSum(nums: List<Int>, m: Int, k: Int): Long {
        val freq = HashMap<Int, Int>()
        var sum = 0L
        var ans = 0L
        for (i in nums.indices) {
            freq[nums[i]] = freq.getOrDefault(nums[i], 0) + 1
            sum += nums[i]
            if (i >= k) {
                val out = nums[i - k]
                sum -= out
                val c = freq.getOrDefault(out, 0) - 1
                if (c == 0) freq.remove(out) else freq[out] = c
            }
            if (i >= k - 1 && freq.size >= m) ans = maxOf(ans, sum)
        }
        return ans
    }
}
