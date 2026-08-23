// LeetCode 2564 - Substring XOR Queries
// https://leetcode.com/problems/substring-xor-queries/

using System.Collections.Generic;

public class Solution {
    public int[][] SubstringXorQueries(string s, int[][] queries) {
        var pos = new Dictionary<int, (int, int)>();
        int n = s.Length;
        for (int i = 0; i < n; ++i) {
            if (s[i] == '0') {
                if (!pos.ContainsKey(0)) pos[0] = (i, i);
                continue;
            }
            int val = 0;
            for (int j = i; j < n && j < i + 30; ++j) {
                val = val * 2 + (s[j] - '0');
                if (!pos.ContainsKey(val)) pos[val] = (i, j);
            }
        }
        int[][] ans = new int[queries.Length][];
        for (int i = 0; i < queries.Length; ++i) {
            int need = queries[i][0] ^ queries[i][1];
            if (pos.TryGetValue(need, out var p)) ans[i] = new[] { p.Item1, p.Item2 };
            else ans[i] = new[] { -1, -1 };
        }
        return ans;
    }
}
