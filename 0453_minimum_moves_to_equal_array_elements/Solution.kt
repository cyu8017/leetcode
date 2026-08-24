// LeetCode 0453 - Minimum Moves to Equal Array Elements
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

class Solution {
    fun minMoves(nums: IntArray): Int {
        val minimum = nums.min()
        return nums.sumOf { it - minimum }
    }
}
