// LeetCode 1842 - Next Palindrome Using Same Digits
// https://leetcode.com/problems/next-palindrome-using-same-digits/

class Solution {
    fun nextPalindrome(num: String): String {
        val nums = num.toCharArray()
        if (!nextPermutation(nums)) return ""
        val n = nums.size
        for (i in 0 until n / 2) {
            nums[n - i - 1] = nums[i]
        }
        return String(nums)
    }

    private fun nextPermutation(nums: CharArray): Boolean {
        val n = nums.size / 2
        var i = n - 2
        while (i >= 0 && nums[i] >= nums[i + 1]) i--
        if (i < 0) return false
        var j = n - 1
        while (nums[j] <= nums[i]) j--
        val tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        var left = i + 1
        var right = n - 1
        while (left < right) {
            val t = nums[left]
            nums[left] = nums[right]
            nums[right] = t
            left++
            right--
        }
        return true
    }
}
