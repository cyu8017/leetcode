// LeetCode 0936 - Stamping The Sequence
// https://leetcode.com/problems/stamping-the-sequence/

using System.Collections.Generic;

public class Solution {
    public int[] MovesToStamp(string stamp, string target) {
        int n = target.Length, m = stamp.Length;
        bool[] done = new bool[n];
        var ans = new List<int>();
        bool changed = true;
        while (changed) {
            changed = false;
            for (int i = n - m; i >= 0; i--) {
                bool ok = true, any = false;
                for (int j = 0; j < m; j++) {
                    if (!done[i + j] && target[i + j] != stamp[j]) { ok = false; break; }
                    if (!done[i + j]) any = true;
                }
                if (ok && any) {
                    for (int j = 0; j < m; j++) done[i + j] = true;
                    ans.Add(i);
                    changed = true;
                    break;
                }
            }
        }
        foreach (bool d in done) if (!d) return new int[0];
        ans.Reverse();
        return ans.ToArray();
    }
}
