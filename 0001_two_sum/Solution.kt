// LeetCode 0001 - Two Sum
// https://leetcode.com/problems/two-sum/

class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val seen = HashMap<Int, Int>()
        for ((i, num) in nums.withIndex()) {
            val complement = target - num
            if (seen.containsKey(complement)) {
                return intArrayOf(seen[complement]!!, i)
            }
            seen[num] = i
        }
        return intArrayOf()
    }
}
