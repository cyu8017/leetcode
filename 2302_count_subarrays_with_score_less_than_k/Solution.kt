// LeetCode 2302 - Count Subarrays With Score Less Than K
// https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

class Solution {

    fun countSubarrays(nums: IntArray, k: Long): Long {

            var ans = 0; var sum = 0
            var left = 0
            for (right in 0 until nums.size) {
                sum += nums[right]
                while (sum * (right - left + 1) >= k) {
                    sum -= nums[left]
                    left++
                }
                ans += right - left + 1
            }
            return ans

    }

}
