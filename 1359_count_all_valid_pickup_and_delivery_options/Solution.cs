// LeetCode 1359 - Count All Valid Pickup And Delivery Options
// https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

public class Solution {
    public int CountOrders(int n) {
        long ans = 1, mod = 1000000007;
        for (int i = 1; i <= n; i++) ans = ans * i * (2 * i - 1) % mod;
        return (int)ans;
    }
}
