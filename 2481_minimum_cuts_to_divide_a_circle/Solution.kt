// LeetCode 2481 - Minimum Cuts to Divide a Circle
// https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/

class Solution {
    fun numberOfCuts(n: Int): Int {
            if (n == 1) return 0
            if (n % 2 == 0) return n / 2
            return n
    }
}
