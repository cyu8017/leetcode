// LeetCode 2391 - Minimum Amount of Time to Collect Garbage
// https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

using System.Collections.Generic;

public class Solution {
    public int GarbageCollection(string[] garbage, int[] travel) {
        int ans = 0;
        var last = new Dictionary<char, int>();
        for (int i = 0; i < garbage.Length; i++) {
            ans += garbage[i].Length;
            foreach (char c in garbage[i]) last[c] = i;
        }
        int[] pref = new int[travel.Length + 1];
        for (int i = 0; i < travel.Length; i++) pref[i + 1] = pref[i] + travel[i];
        foreach (char typ in new[] { 'M', 'P', 'G' }) {
            if (last.TryGetValue(typ, out int idx)) ans += pref[idx];
        }
        return ans;
    }
}
