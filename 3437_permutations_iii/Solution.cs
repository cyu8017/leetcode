// LeetCode 3437 - Permutations III
// https://leetcode.com/problems/permutations-iii/

using System.Collections.Generic;

public class Solution {
    public int[][] Permute(int n) {
        var ans = new List<int[]>();
        bool[] used = new bool[n + 1];
        var cur = new List<int>();
        void Dfs() {
            if (cur.Count == n) {
                ans.Add(cur.ToArray());
                return;
            }
            for (int i = 1; i <= n; i++) {
                if (used[i]) continue;
                if (cur.Count > 0 && (cur[cur.Count - 1] % 2 == i % 2)) continue;
                used[i] = true;
                cur.Add(i);
                Dfs();
                cur.RemoveAt(cur.Count - 1);
                used[i] = false;
            }
        }
        Dfs();
        return ans.ToArray();
    }
}
