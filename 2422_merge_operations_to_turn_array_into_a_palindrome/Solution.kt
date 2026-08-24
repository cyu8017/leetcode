// LeetCode 2422 - Merge Operations to Turn Array Into a Palindrome
// https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/

class Solution {
    fun minimumOperations(nums: IntArray): Int {
            var l: Int = 0
            var r: Int = nums.size - 1
            var left: Long = nums[l]
            var right: Long = nums[r]
            var ans: Int = 0
            while (l < r) {
                if (left == right) {
                    l = l + 1
                    r = r - 1
                    if (l < r) {
                        left = nums[l]
                        right = nums[r]
                    }
                } else if (left < right) {
                    l = l + 1
                    left +=nums[l]
                    ans = ans + 1
                } else {
                    r = r - 1
                    right +=nums[r]
                    ans = ans + 1
                }
            }
            return ans
    }
}
