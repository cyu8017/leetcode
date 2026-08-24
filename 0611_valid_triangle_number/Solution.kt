// LeetCode 0611 - Valid Triangle Number
// https://leetcode.com/problems/valid-triangle-number/


class Solution {
    fun triangleNumber(nums: IntArray): Int {
        nums.sort()
        var count = 0
        for (k in nums.size - 1 downTo 2) {
            var i = 0
            var j = k - 1
            while (i < j) {
                if (nums[i] + nums[j] > nums[k]) {
                    count += j - i
                    j--
                } else {
                    i++
                }
            }
        }
        return count
    }
}
