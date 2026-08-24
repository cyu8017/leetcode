// LeetCode 3638 - Maximum Balanced Shipments
// https://leetcode.com/problems/maximum-balanced-shipments/

class Solution {
    fun maxBalancedShipments(weight: IntArray): Int {
        var ans = 0
        var mx = 0
        for (x in weight) {
            mx = maxOf(mx, x)
            if (x < mx) {
                ans++
                mx = 0
            }
        }
        return ans
    }
}
