// LeetCode 0575 - Distribute Candies
// https://leetcode.com/problems/distribute-candies/


class Solution {
    fun distributeCandies(candyType: IntArray): Int {
        return minOf(candyType.toSet().size, candyType.size / 2)
    }
}
