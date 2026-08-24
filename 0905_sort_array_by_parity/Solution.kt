// LeetCode 0905 - Sort Array By Parity
// https://leetcode.com/problems/sort-array-by-parity/

class Solution {
    fun sortArrayByParity(nums: IntArray): IntArray {
        var i = 0
        for (j in 0 until nums.size) {
            if (nums[j] % 2 == 0) {
                var tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i++
            }
        }
        return nums
    }
}
