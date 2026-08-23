// LeetCode 3527 - Find the Most Common Response
// https://leetcode.com/problems/find-the-most-common-response/

using System.Collections.Generic;

public class Solution {
    public string FindCommonResponse(IList<IList<string>> responses) {
        var cnt = new Dictionary<string, int>();
        foreach (var ws in responses) {
            var s = new HashSet<string>();
            foreach (var w in ws) {
                if (s.Add(w)) {
                    if (!cnt.ContainsKey(w)) cnt[w] = 0;
                    cnt[w]++;
                }
            }
        }
        string ans = responses[0][0];
        foreach (var kv in cnt) {
            string w = kv.Key;
            int v = kv.Value;
            if (cnt[ans] < v || (cnt[ans] == v && string.CompareOrdinal(w, ans) < 0)) ans = w;
        }
        return ans;
    }
}
