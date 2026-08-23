// LeetCode 3988 - Create Grid With Exactly K Paths I
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-i/

using System.Collections.Generic;

public class Solution {
    public string[] CreateGrid(int m, int n, int k) {
        var cands = new List<string[]>();
        if (k == 1) cands.Add(new[] { "." });
        else if (k == 2) cands.Add(new[] { "..", ".." });
        else if (k == 3) {
            cands.Add(new[] { "..", "..", ".." });
            cands.Add(new[] { "...", "..." });
        } else if (k == 4) {
            cands.Add(new[] { "..", "..", "..", ".." });
            cands.Add(new[] { "....", "...." });
            cands.Add(new[] { "..#", "...", "#.." });
        }
        foreach (var pat in cands) {
            int pr = pat.Length;
            int pc = pat[0].Length;
            if (pr > m || pc > n) continue;
            string[] result = new string[m];
            for (int i = 0; i < m; i++) {
                char[] row = new char[n];
                for (int j = 0; j < n; j++) row[j] = '#';
                result[i] = new string(row);
            }
            for (int i = 0; i < pr; i++) {
                char[] row = result[i].ToCharArray();
                for (int j = 0; j < pc; j++) row[j] = pat[i][j];
                result[i] = new string(row);
            }
            for (int i = pr; i < m; i++) {
                char[] row = result[i].ToCharArray();
                row[pc - 1] = '.';
                result[i] = new string(row);
            }
            for (int j = pc; j < n; j++) {
                char[] row = result[m - 1].ToCharArray();
                row[j] = '.';
                result[m - 1] = new string(row);
            }
            return result;
        }
        return new string[0];
    }
}
