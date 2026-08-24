// LeetCode 1744 - Can You Eat Your Favorite Candy on Your Favorite Day?
// https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/

class Solution {
    fun canEat(candiesCount: IntArray, queries: Array<IntArray>): BooleanArray {
        val prefix = LongArray(candiesCount.size + 1)
        for (i in candiesCount.indices) {
            prefix[i + 1] = prefix[i] + candiesCount[i]
        }
        val ans = BooleanArray(queries.size)
        for (i in queries.indices) {
            val candyType = queries[i][0]
            val day = queries[i][1].toLong()
            val cap = queries[i][2].toLong()
            val minEaten = day + 1
            val maxEaten = (day + 1) * cap
            ans[i] = maxEaten > prefix[candyType] && minEaten <= prefix[candyType + 1]
        }
        return ans
    }
}
