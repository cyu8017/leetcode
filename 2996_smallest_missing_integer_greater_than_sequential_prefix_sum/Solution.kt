// LeetCode 2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum
// https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

class Solution {
    fun missingInteger(nums: IntArray): Int {
        var sum = nums[0]
        for (i in 1 until nums.size && nums[i] == nums[i - 1] + 1) {
            sum += nums[i]
        }
        var seen = HashSet<Int>()
        for (v in nums) { seen.add(v) }
        while (seen.contains(sum)) sum++
        return sum
    }
}
