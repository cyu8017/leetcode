// LeetCode 3736 - Minimum Moves to Equal Array Elements III
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

class Solution {
    fun minMoves(nums: IntArray): Int {
        var mx = 0
        var s = 0
        for (x in nums) {
            mx = maxOf(mx, x)
            s += x
        }
        return mx * nums.size - s
    }
}
