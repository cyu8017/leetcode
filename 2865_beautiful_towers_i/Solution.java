// LeetCode 2865 - Beautiful Towers I
// https://leetcode.com/problems/beautiful-towers-i/

import java.util.List;

class Solution {
    public long maximumSumOfHeights(List<Integer> heights) {
        int n = heights.size();
        long ans = 0;
        for (int peak = 0; peak < n; peak++) {
            long sum = heights.get(peak);
            int mn = heights.get(peak);
            for (int i = peak - 1; i >= 0; i--) {
                if (heights.get(i) < mn) mn = heights.get(i);
                sum += mn;
            }
            mn = heights.get(peak);
            for (int i = peak + 1; i < n; i++) {
                if (heights.get(i) < mn) mn = heights.get(i);
                sum += mn;
            }
            if (sum > ans) ans = sum;
        }
        return ans;
    }
}
