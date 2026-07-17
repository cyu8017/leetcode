// LeetCode 1785 - Minimum Elements to Add to Form a Given Sum
// https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/

class Solution {
    fun minElements(nums: IntArray, limit: Int, goal: Int): Int {
        var sum = 0L
        for (num in nums) {
            sum += num
        }
        val diff = Math.abs(sum - goal)
        return ((diff + limit - 1) / limit).toInt()
    }
}
