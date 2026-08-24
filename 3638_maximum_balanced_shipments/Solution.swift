// LeetCode 3638 - Maximum Balanced Shipments
// https://leetcode.com/problems/maximum-balanced-shipments/

class Solution {
    func maxBalancedShipments(_ weight: [Int]) -> Int {
        var ans = 0, mx = 0
        for x in weight {
            mx = max(mx, x)
            if x < mx {
                ans += 1
                mx = 0
            }
        }
        return ans
    }
}
