// LeetCode 3160 - Find the Number of Distinct Colors Among the Balls
// https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

using System.Collections.Generic;

public class Solution {
    public int[] QueryResults(int limit, int[][] queries) {
        var g = new Dictionary<int, int>();
        var cnt = new Dictionary<int, int>();
        int[] ans = new int[queries.Length];
        for (int qi = 0; qi < queries.Length; qi++) {
            int x = queries[qi][0], y = queries[qi][1];
            if (!cnt.ContainsKey(y)) cnt[y] = 0;
            cnt[y]++;
            if (g.TryGetValue(x, out int old)) {
                if (--cnt[old] == 0) cnt.Remove(old);
            }
            g[x] = y;
            ans[qi] = cnt.Count;
        }
        return ans;
    }
}
