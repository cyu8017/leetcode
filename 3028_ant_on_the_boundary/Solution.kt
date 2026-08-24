// LeetCode 3028 - Ant on the Boundary
// https://leetcode.com/problems/ant-on-the-boundary/

class Solution {
    fun returnToBoundaryCount(nums: IntArray): Int {
        var s = 0
        var ans = 0
        for (x in nums) {
            s += x
            if (s == 0) ans++
        }
        return ans
    }
}
