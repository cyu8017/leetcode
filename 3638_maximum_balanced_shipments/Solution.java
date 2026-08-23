// LeetCode 3638 - Maximum Balanced Shipments
// https://leetcode.com/problems/maximum-balanced-shipments/

class Solution {
    public int maxBalancedShipments(int[] weight) {
        int ans = 0, mx = 0;
        for (int x : weight) {
            mx = Math.max(mx, x);
            if (x < mx) {
                ans++;
                mx = 0;
            }
        }
        return ans;
    }
}
