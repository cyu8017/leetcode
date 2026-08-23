// LeetCode 3237 - Alt and Tab Simulation
// https://leetcode.com/problems/alt-and-tab-simulation/

using System.Collections.Generic;

public class Solution {
    public int[] SimulationResult(int[] windows, int[] queries) {
        int n = windows.Length;
        bool[] s = new bool[n + 1];
        var ans = new List<int>();
        for (int i = queries.Length - 1; i >= 0; i--) {
            int q = queries[i];
            if (!s[q]) {
                s[q] = true;
                ans.Add(q);
            }
        }
        foreach (int w in windows) {
            if (!s[w]) ans.Add(w);
        }
        return ans.ToArray();
    }
}
