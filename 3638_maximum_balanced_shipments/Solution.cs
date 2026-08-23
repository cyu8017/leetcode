// LeetCode 3638 - Maximum Balanced Shipments
// https://leetcode.com/problems/maximum-balanced-shipments/

using System;

public class Solution {
    public int MaxBalancedShipments(int[] weight) {
        int ans = 0, mx = 0;
        foreach (int x in weight) {
            mx = Math.Max(mx, x);
            if (x < mx) {
                ans++;
                mx = 0;
            }
        }
        return ans;
    }
}
