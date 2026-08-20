// LeetCode 1359 - Count All Valid Pickup and Delivery Options
// https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

class Solution {
    func countOrders(_ n: Int) -> Int {
        let mod = 1_000_000_007
        var ans = 1
        for i in 1...n {
            ans = ans * i % mod * (2 * i - 1) % mod
        }
        return ans
    }
}
