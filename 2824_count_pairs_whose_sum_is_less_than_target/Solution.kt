// LeetCode 2824 - Count Pairs Whose Sum is Less than Target
// https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution {
    fun countPairs(nums: MutableList<Int>, target: Int): Int {
        var ans = 0
        for (i in nums.indices) {
            for (j in i + 1 until nums.size) {
                if (nums[i] + nums[j] < target) ans++
            }
        }
        return ans
    }
}
