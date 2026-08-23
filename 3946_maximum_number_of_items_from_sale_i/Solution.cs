// LeetCode 3946 - Maximum Number Of Items From Sale I
// https://leetcode.com/problems/maximum-number-of-items-from-sale-i/

using System;

public class Solution {
    public int MaximumSaleItems(int[][] items, int budget) {
        int[] f = new int[budget + 1];
        int mn = int.MaxValue;
        foreach (var item in items) {
            int factor = item[0], price = item[1];
            mn = Math.Min(mn, price);
            int cnt = 0;
            foreach (var jItem in items) {
                if (jItem[0] % factor == 0) cnt++;
            }
            for (int j = budget; j >= price; j--) {
                f[j] = Math.Max(f[j], f[j - price] + cnt);
            }
        }
        int ans = 0;
        for (int i = 0; i <= budget; i++) {
            int extra = (budget - i) / mn;
            ans = Math.Max(ans, f[i] + extra);
        }
        return ans;
    }
}
