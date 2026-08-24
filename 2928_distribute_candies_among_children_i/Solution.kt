// LeetCode 2928 - Distribute Candies Among Children I
// https://leetcode.com/problems/distribute-candies-among-children-i/


class Solution {
    fun distributeCandies(n: Int, limit: Int): Int {
        var ans = 0
        for (i in 0..limit) {
            for (j in 0..limit) {
                val k = n - i - j
                if (k in 0..limit) ans++
            }
        }
        return ans
    }
}
