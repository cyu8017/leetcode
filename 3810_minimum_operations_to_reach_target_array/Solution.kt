// LeetCode 3810 - Minimum Operations To Reach Target Array
// https://leetcode.com/problems/minimum-operations-to-reach-target-array/

class Solution {
    fun minOperations(nums: IntArray, target: IntArray): Int {
        var s = HashSet<Int>()
        for (i in 0 until nums.size) {
            if (nums[i] != target[i]) s.add(nums[i])
        }
        return s.size
    }
}
