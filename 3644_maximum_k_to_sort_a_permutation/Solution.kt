// LeetCode 3644 - Maximum K to Sort a Permutation
// https://leetcode.com/problems/maximum-k-to-sort-a-permutation/

class Solution {
    fun sortPermutation(nums: IntArray): Int {
        var ans = -1
        for (i in nums.indices) {
            if (i != nums[i]) ans = ans and nums[i]
        }
        return maxOf(ans, 0)
    }
}
