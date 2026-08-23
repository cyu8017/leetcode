// LeetCode 2085 - Count Common Words With One Occurrence
// https://leetcode.com/problems/count-common-words-with-one-occurrence/

using System.Collections.Generic;

public class Solution {
    public int CountWords(string[] words1, string[] words2) {
        var f1 = new Dictionary<string, int>();
        var f2 = new Dictionary<string, int>();
        foreach (var w in words1) { if (!f1.ContainsKey(w)) f1[w] = 0; f1[w]++; }
        foreach (var w in words2) { if (!f2.ContainsKey(w)) f2[w] = 0; f2[w]++; }
        int ans = 0;
        foreach (var kv in f1)
            if (kv.Value == 1 && f2.TryGetValue(kv.Key, out int c) && c == 1) ans++;
        return ans;
    }
}
