// LeetCode 1276 - Number of Burgers with No Waste of Ingredients
// https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

class Solution {
    fun numOfBurgers(tomatoSlices: Int, cheeseSlices: Int): List<Int> {
        if (tomatoSlices % 2 != 0) return emptyList()
        val jumbo = tomatoSlices / 2 - cheeseSlices
        val small = cheeseSlices - jumbo
        return if (jumbo >= 0 && small >= 0) listOf(jumbo, small) else emptyList()
    }
}
