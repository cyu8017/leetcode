// LeetCode 3680 - Generate Schedule
// https://leetcode.com/problems/generate-schedule/

using System.Collections.Generic;

public class Solution {
    public int[][] GenerateSchedule(int n) {
        if (n < 5) return System.Array.Empty<int[]>();
        var matches = new List<int[]>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j) matches.Add(new[] { i, j });
            }
        }
        bool[] used = new bool[matches.Count];
        var sched = new List<int[]>();
        int last0 = -1, last1 = -1;
        bool Dfs() {
            if (sched.Count == matches.Count) return true;
            for (int i = 0; i < matches.Count; i++) {
                if (used[i]) continue;
                var m = matches[i];
                if (m[0] == last0 || m[0] == last1 || m[1] == last0 || m[1] == last1) continue;
                used[i] = true;
                sched.Add(m);
                int p0 = last0, p1 = last1;
                last0 = m[0]; last1 = m[1];
                if (Dfs()) return true;
                last0 = p0; last1 = p1;
                sched.RemoveAt(sched.Count - 1);
                used[i] = false;
            }
            return false;
        }
        if (Dfs()) return sched.ToArray();
        return System.Array.Empty<int[]>();
    }
}
