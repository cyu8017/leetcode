// LeetCode 2270 - Number of Ways to Split Array
// https://leetcode.com/problems/number-of-ways-to-split-array/

class Solution {

    fun waysToSplitArray(nums: IntArray): Int {

            var total = 0
            for (v in nums) total += v
            var left = 0
            var ans = 0
            run {
    var i = 0
    while (i + 1 < nums.size) {

                left += nums[i]
                if (left >= total - left) ans++

    i++
    }
    }
            return ans

    }

}
