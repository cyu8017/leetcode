// LeetCode 2517 - Maximum Tastiness of Candy Basket
// https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

using System;

public class Solution {
    public int MaximumTastiness(int[] price, int k) {
        Array.Sort(price);
        bool Ok(int d) {
            int cnt = 1, last = price[0];
            for (int i = 1; i < price.Length; i++) {
                if (price[i] - last >= d) {
                    cnt++;
                    last = price[i];
                    if (cnt >= k) return true;
                }
            }
            return false;
        }
        int lo = 0, hi = price[price.Length - 1] - price[0];
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (Ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}
