// LeetCode 1051 - Height Checker
// https://leetcode.com/problems/height-checker/

import java.util.Arrays;

class Solution {
    public int heightChecker(int[] heights) {
        int[] sorted = heights.clone();
        Arrays.sort(sorted);
        int ans = 0;
        for (int i = 0; i < heights.length; i++) {
            if (heights[i] != sorted[i]) {
                ans++;
            }
        }
        return ans;
    }
}
