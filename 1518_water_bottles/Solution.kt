// LeetCode 1518 - Water Bottles
// https://leetcode.com/problems/water-bottles/

class Solution {
    fun numWaterBottles(numBottles: Int, numExchange: Int): Int {
        var bottles = numBottles
        var total = bottles
        while (bottles >= numExchange) {
            val newBottles = bottles / numExchange
            val remainder = bottles % numExchange
            total += newBottles
            bottles = newBottles + remainder
        }
        return total
    }
}
