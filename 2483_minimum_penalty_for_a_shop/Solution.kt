// LeetCode 2483 - Minimum Penalty for a Shop
// https://leetcode.com/problems/minimum-penalty-for-a-shop/

class Solution {
    fun bestClosingTime(customers: String): Int {
        val n = customers.length
        var penalty = 0
        for (c in customers) if (c == 'Y') penalty++
        var best = penalty
        var ans = 0
        for (i in 0 until n) {
            if (customers[i] == 'Y') penalty-- else penalty++
            if (penalty < best) {
                best = penalty
                ans = i + 1
            }
        }
        return ans
    }
}
