// LeetCode 3450 - Maximum Students on a Single Bench
// https://leetcode.com/problems/maximum-students-on-a-single-bench/

using System.Collections.Generic;

public class Solution {
    public int MaxStudentsOnBench(int[][] students) {
        var bench = new Dictionary<int, HashSet<int>>();
        foreach (var s in students) {
            int sid = s[0], b = s[1];
            if (!bench.ContainsKey(b)) bench[b] = new HashSet<int>();
            bench[b].Add(sid);
        }
        int ans = 0;
        foreach (var kv in bench) {
            if (kv.Value.Count > ans) ans = kv.Value.Count;
        }
        return ans;
    }
}
