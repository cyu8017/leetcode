// LeetCode 3889 - Mirror Frequency Distance
// https://leetcode.com/problems/mirror-frequency-distance/

using System;
using System.Collections.Generic;

public class Solution {
    public int MirrorFrequency(string s) {
        var freq = new Dictionary<char, int>();
        foreach (char c in s) {
            if (!freq.ContainsKey(c)) freq[c] = 0;
            freq[c]++;
        }
        int ans = 0;
        var vis = new Dictionary<char, bool>();
        foreach (var kv in freq) {
            char c = kv.Key;
            int v = kv.Value;
            char m;
            if (c >= 'a' && c <= 'z') m = (char)('a' + 25 - (c - 'a'));
            else m = (char)('0' + (9 - (c - '0')));
            if (vis.ContainsKey(m) && vis[m]) continue;
            vis[c] = true;
            int mv = freq.ContainsKey(m) ? freq[m] : 0;
            ans += Math.Abs(v - mv);
        }
        return ans;
    }
}
