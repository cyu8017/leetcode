// LeetCode 2239 - Find Closest Number to Zero
// https://leetcode.com/problems/find-closest-number-to-zero/

class Solution {

    fun findClosestNumber(nums: IntArray): Int {

            var ans = nums[0]
            for (x in nums) {
                if (kotlin.math.abs(x) < kotlin.math.abs(ans) || (kotlin.math.abs(x) == kotlin.math.abs(ans) && x > ans)) ans = x
            }
            return ans

    }

}
