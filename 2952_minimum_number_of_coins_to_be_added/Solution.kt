// LeetCode 2952 - Minimum Number of Coins to be Added
// https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

class Solution {
    fun minimumAddedCoins(coins: IntArray, target: Int): Int {
        coins.sort()
        var ans = 0
        var reach = 0
        var i = 0
        while (reach < target) {
            if (i < coins.size && coins[i] <= reach + 1) {
                reach += coins[i]
                i++
            } else {
                reach += reach + 1
                ans++
            }
        }
        return ans
    }
}
