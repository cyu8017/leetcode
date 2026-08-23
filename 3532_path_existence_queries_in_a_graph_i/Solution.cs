// LeetCode 3532 - Path Existence Queries in a Graph I
// https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

public class Solution {
    public bool[] PathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        int[] g = new int[n];
        int cnt = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] - nums[i - 1] > maxDiff) cnt++;
            g[i] = cnt;
        }
        bool[] ans = new bool[queries.Length];
        for (int i = 0; i < queries.Length; i++)
            ans[i] = g[queries[i][0]] == g[queries[i][1]];
        return ans;
    }
}
