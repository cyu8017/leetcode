// LeetCode 1431 - Kids With the Greatest Number of Candies
// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution {
    fun kidsWithCandies(candies: IntArray, extraCandies: Int): List<Boolean> {
        val maximum = candies.maxOrNull() ?: 0
        return candies.map { it + extraCandies >= maximum }
    }
}
