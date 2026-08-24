// CONFIG class=Solution method=maximumSaleItems types=None
// LeetCode 3946 - Maximum Number Of Items From Sale I
// https://leetcode.com/problems/maximum-number-of-items-from-sale-i/

class Solution {
    public int maximumSaleItems(int[][] items, int budget) {
        int[] f = new int[budget + 1];
        int mn = Integer.MAX_VALUE;
        for (var item : items) {
            int factor = item[0], price = item[1];
            mn = Math.min(mn, price);
            int cnt = 0;
            for (var jItem : items) {
                if (jItem[0] % factor == 0) cnt++;
            }
            for (int j = budget; j >= price; j--) {
                f[j] = Math.max(f[j], f[j - price] + cnt);
            }
        }
        int ans = 0;
        for (int i = 0; i <= budget; i++) {
            int extra = (budget - i) / mn;
            ans = Math.max(ans, f[i] + extra);
        }
        return ans;
    }
}
