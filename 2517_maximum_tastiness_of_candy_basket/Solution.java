// LeetCode 2517 - Maximum Tastiness of Candy Basket
// https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

import java.util.Arrays;

class Solution {
    public int maximumTastiness(int[] price, int k) {
        Arrays.sort(price);
        boolean ok(int d) {
            int cnt = 1, last = price[0];
            for (int i = 1; i < price.length; i++) {
                if (price[i] - last >= d) {
                    cnt++;
                    last = price[i];
                    if (cnt >= k) return true;
                }
            }
            return false;
        }
        int lo = 0, hi = price[price.length - 1] - price[0];
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (Ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}
