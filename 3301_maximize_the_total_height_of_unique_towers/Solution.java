// LeetCode 3301 - Maximize the Total Height of Unique Towers
// https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/

import java.util.Arrays;

class Solution {
    public long maximumTotalSum(int[] maximumHeight) {
        Arrays.sort(maximumHeight);
        for (int i = 0, j = maximumHeight.length - 1; i < j; i++, j--) {
            int t = maximumHeight[i];
            maximumHeight[i] = maximumHeight[j];
            maximumHeight[j] = t;
        }
        long ans = 0;
        long prev = (long) 1e18;
        for (int h : maximumHeight) {
            long cur = h;
            if (cur >= prev) cur = prev - 1;
            if (cur <= 0) return -1;
            ans += cur;
            prev = cur;
        }
        return ans;
    }
}
