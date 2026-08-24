// LeetCode 2229 - Check if an Array Is Consecutive
// https://leetcode.com/problems/check-if-an-array-is-consecutive/

class Solution {

    fun isConsecutive(nums: IntArray): Boolean {

            var mn = nums[0]; var mx = nums[0]
            var seen = HashSet<Int>()
            for (x in nums) {
                if (!seen.add(x)) return false
                mn = minOf(mn, x)
                mx = maxOf(mx, x)
            }
            return mx - mn + 1 == nums.size

    }

}
