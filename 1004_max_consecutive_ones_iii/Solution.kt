// LeetCode 1004 - Max Consecutive Ones III
// https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution {
    fun longestOnes(nums: IntArray, k: Int): Int {
        var left = 0; var zeros = 0; var ans = 0
        for (right in nums.indices) {
            if (nums[right] == 0) zeros++
            while (zeros > k) {
                if (nums[left++] == 0) zeros--
            }
            ans = maxOf(ans, right - left + 1)
        }
        return ans
    }
}
