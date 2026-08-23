// LeetCode 0884 - Uncommon Words from Two Sentences
// https://leetcode.com/problems/uncommon-words-from-two-sentences/

using System.Collections.Generic;

public class Solution {
    public string[] UncommonFromSentences(string s1, string s2) {
        var count = new Dictionary<string, int>();
        void Add(string s) {
            foreach (var w in s.Split(new[] { ' ' }, System.StringSplitOptions.RemoveEmptyEntries)) {
                if (!count.ContainsKey(w)) count[w] = 0;
                count[w]++;
            }
        }
        Add(s1);
        Add(s2);
        var ans = new List<string>();
        foreach (var kv in count) if (kv.Value == 1) ans.Add(kv.Key);
        return ans.ToArray();
    }
}
