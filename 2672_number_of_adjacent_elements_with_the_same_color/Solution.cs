// LeetCode 2672 - Number of Adjacent Elements With the Same Color
// https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

public class Solution {
    public int[] ColorTheArray(int n, int[][] queries) {
        int[] colors = new int[n], ans = new int[queries.Length];
        int same = 0;
        for (int i = 0; i < queries.Length; i++) {
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
