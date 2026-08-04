// LeetCode 1561 - Maximum Number of Coins You Can Get
// https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution {
    fun maxCoins(piles: IntArray): Int {
        piles.sort()
        var sum = 0
        var i = piles.size / 3
        while (i < piles.size) {
            sum += piles[i]
            i += 2
        }
        return sum
    }
}
