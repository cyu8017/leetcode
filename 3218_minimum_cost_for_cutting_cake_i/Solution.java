// LeetCode 3218 - Minimum Cost for Cutting Cake I
// https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/

import java.util.Arrays;

class Solution {
    public int minimumCost(int m, int n, int[] horizontalCut, int[] verticalCut) {
        Arrays.sort(horizontalCut);
        reverse(horizontalCut);
        Arrays.sort(verticalCut);
        reverse(verticalCut);
        int i = 0, j = 0, h = 1, v = 1, ans = 0;
        while (i < m - 1 || j < n - 1) {
            if (j == n - 1 || (i < m - 1 && horizontalCut[i] > verticalCut[j])) {
                ans += horizontalCut[i] * v;
                h++; i++;
            } else {
                ans += verticalCut[j] * h;
                v++; j++;
            }
        }
        return ans;
    }

    private void reverse(int[] a) {
        for (int l = 0, r = a.length - 1; l < r; l++, r--) {
            int t = a[l]; a[l] = a[r]; a[r] = t;
        }
    }
}
