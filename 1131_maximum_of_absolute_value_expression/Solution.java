// LeetCode 1131 - Maximum of Absolute Value Expression
// https://leetcode.com/problems/maximum-of-absolute-value-expression/

class Solution {
    public int maxAbsValExpr(int[] arr1, int[] arr2) {
        int n = arr1.length, ans = 0;
        int[][] signs = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
        for (int[] s : signs) {
            int best = s[0] * arr1[0] + s[1] * arr2[0];
            for (int i = 1; i < n; i++) {
                int cur = s[0] * arr1[i] + s[1] * arr2[i] + i;
                ans = Math.max(ans, cur - best);
                best = Math.min(best, s[0] * arr1[i] + s[1] * arr2[i] + i);
            }
        }
        return ans;
    }
}
