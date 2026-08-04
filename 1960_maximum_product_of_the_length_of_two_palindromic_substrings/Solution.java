// LeetCode 1960 - Maximum Product of the Length of Two Palindromic Substrings
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/

import java.util.*;

class Solution {
    public long maxProduct(String s) {
        int n = s.length();
        int[] radius = new int[n];
        int center = 0, right = 0;
        for (int i = 0; i < n; i++) {
            if (i < right) radius[i] = Math.min(right - i, radius[2 * center - i]);
            while (i - radius[i] - 1 >= 0 && i + radius[i] + 1 < n
                    && s.charAt(i - radius[i] - 1) == s.charAt(i + radius[i] + 1)) {
                radius[i]++;
            }
            if (i + radius[i] > right) {
                center = i;
                right = i + radius[i];
            }
        }
        int[] end = new int[n], start = new int[n];
        Arrays.fill(end, 1);
        Arrays.fill(start, 1);
        for (int i = 0; i < n; i++) {
            int r = radius[i];
            end[i + r] = Math.max(end[i + r], 2 * r + 1);
            start[i - r] = Math.max(start[i - r], 2 * r + 1);
        }
        for (int i = n - 2; i >= 0; i--) end[i] = Math.max(end[i], end[i + 1] - 2);
        for (int i = 1; i < n; i++) start[i] = Math.max(start[i], start[i - 1] - 2);
        int[] pre = new int[n], suf = new int[n];
        pre[0] = end[0];
        for (int i = 1; i < n; i++) pre[i] = Math.max(pre[i - 1], end[i]);
        suf[n - 1] = start[n - 1];
        for (int i = n - 2; i >= 0; i--) suf[i] = Math.max(suf[i + 1], start[i]);
        long ans = 0;
        for (int i = 0; i < n - 1; i++) ans = Math.max(ans, (long) pre[i] * suf[i + 1]);
        return ans;
    }
}
