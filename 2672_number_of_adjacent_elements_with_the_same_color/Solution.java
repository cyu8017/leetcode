// LeetCode 2672 - Number of Adjacent Elements With the Same Color
// https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

class Solution {
    public int[] colorTheArray(int n, int[][] queries) {
        int[] colors = new int[n], ans = new int[queries.length];
        int same = 0;
        for (int i = 0; i < queries.length; i++) {
            int idx = queries[i][0], color = queries[i][1];
            if (colors[idx] != 0) {
                if (idx > 0 && colors[idx] == colors[idx - 1]) same--;
                if (idx + 1 < n && colors[idx] == colors[idx + 1]) same--;
            }
            colors[idx] = color;
            if (idx > 0 && colors[idx] == colors[idx - 1]) same++;
            if (idx + 1 < n && colors[idx] == colors[idx + 1]) same++;
            ans[i] = same;
        }
        return ans;
    }
}
