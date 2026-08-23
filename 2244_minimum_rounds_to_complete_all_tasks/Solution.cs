// LeetCode 2244 - Minimum Rounds to Complete All Tasks
// https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

using System.Collections.Generic;

public class Solution {
    public int MinimumRounds(int[] tasks) {
        var freq = new Dictionary<int, int>();
        foreach (int t in tasks) {
            freq.TryGetValue(t, out int c);
            freq[t] = c + 1;
        }
        int ans = 0;
        foreach (int c in freq.Values) {
            if (c == 1) return -1;
            ans += (c + 2) / 3;
        }
        return ans;
    }
}
