// LeetCode 3100 - Water Bottles II
// https://leetcode.com/problems/water-bottles-ii/

class Solution {
    fun maxBottlesDrunk(numBottles: Int, numExchange: Int): Int {
        var ans = numBottles
        while (numBottles >= numExchange) {
            numBottles -= numExchange
            numExchange++
            ans++
            numBottles++
        }
        return ans
    }
}
