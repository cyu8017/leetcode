// LeetCode 2294 - Partition Array Such That Maximum Difference Is K
// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

class Solution {

    fun partitionArray(nums: IntArray, k: Int): Int {

            nums.sort()
            var ans = 1; var start = nums[0]
            for (i in 1 until nums.size) {
                if (nums[i] - start > k) { ans++; start = nums[i]; }
            }
            return ans

    }

}
