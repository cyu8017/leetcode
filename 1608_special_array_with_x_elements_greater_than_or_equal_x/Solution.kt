// LeetCode 1608 - Special Array With X Elements Greater Than or Equal X
// https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution {
    fun specialArray(nums: IntArray): Int {
        for (x in 0..nums.size) {
            if (nums.count { it >= x } == x) return x
        }
        return -1
    }
}
