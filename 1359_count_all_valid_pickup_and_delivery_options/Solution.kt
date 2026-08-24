// LeetCode 1359 - Count All Valid Pickup and Delivery Options
// https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

class Solution {
    fun countOrders(n: Int): Int {
        var ans = 1L
        val mod = 1_000_000_007L
        for (i in 1..n) {
            ans = ans * i % mod * (2L * i - 1) % mod
        }
        return ans.toInt()
    }
}
