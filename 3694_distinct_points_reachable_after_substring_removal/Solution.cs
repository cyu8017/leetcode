// LeetCode 3694 - Distinct Points Reachable After Substring Removal
// https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/

using System.Collections.Generic;

public class Solution {
    public int DistinctPoints(string s, int k) {
        int n = s.Length;
        int[] f = new int[n + 1], g = new int[n + 1];
        int x = 0, y = 0;
        for (int i = 1; i <= n; i++) {
            char c = s[i - 1];
            if (c == 'U') y++;
            else if (c == 'D') y--;
            else if (c == 'L') x--;
            else x++;
            f[i] = x;
            g[i] = y;
        }
        var st = new HashSet<long>();
        for (int i = k; i <= n; i++) {
            int a = f[n] - (f[i] - f[i - k]);
            int b = g[n] - (g[i] - g[i - k]);
            long key = (long)a * n + b;
            st.Add(key);
        }
        return st.Count;
    }
}
