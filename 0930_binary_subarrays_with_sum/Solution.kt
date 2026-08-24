// LeetCode 0930 - Binary Subarrays With Sum
// https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution {
    fun numSubarraysWithSum(nums: IntArray, goal: Int): Int {
        var count = HashMap()
        count.put(0, 1)
        var prefix = 0
        var ans = 0
        for (x in nums) {
            prefix += x
            ans += count.getOrDefault(prefix - goal, 0)
            count.put(prefix, count.getOrDefault(prefix, 0) + 1)
        }
        return ans
    }
}
