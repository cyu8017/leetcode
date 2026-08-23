// LeetCode 3534 - Path Existence Queries in a Graph II
// https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        int[][] pairs = new int[n][2];
        for (int i = 0; i < n; i++) pairs[i] = new int[] {nums[i], i};
        Arrays.sort(pairs, (a, b) -> Integer.compare(a[0], b[0]));
        int m = 20;
        int[][] f = new int[n][m];
        int r = n - 1;
        for (int l = n - 1; l >= 0; l--) {
            while (pairs[r][0] - pairs[l][0] > maxDiff) r--;
            int i = pairs[l][1], j = pairs[r][1];
            f[i][0] = j;
            for (int k = 1; k < m; k++) f[i][k] = f[f[i][k - 1]][k - 1];
        }
        List<Integer> ans = new ArrayList<>();
        for (int[] q : queries) {
            int i = q[0], j = q[1];
            if (nums[i] > nums[j]) { int tmp = i; i = j; j = tmp; }
            if (i == j) { ans.add(0); continue; }
            if (nums[i] == nums[j]) { ans.add(1); continue; }
            int d = 0;
            for (int k = m - 1; k >= 0; k--) {
                if (nums[f[i][k]] < nums[j]) {
                    d |= 1 << k;
                    i = f[i][k];
                }
            }
            if (nums[f[i][0]] < nums[j]) ans.add(-1);
            else ans.add(d + 1);
        }
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }
}
