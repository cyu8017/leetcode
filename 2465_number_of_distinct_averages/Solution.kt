// LeetCode 2465 - Number of Distinct Averages
// https://leetcode.com/problems/number-of-distinct-averages/

import java.util.HashSet

class Solution {
    fun distinctAverages(nums: IntArray): Int {
            nums.sort()
            var seen = HashSet()
            var l: Int = 0
            var r: Int = nums.size - 1
            while (l < r) {
                seen.add(nums[l] + nums[r])
                l = l + 1
                r = r - 1
            }
            return seen.size
    }
}
