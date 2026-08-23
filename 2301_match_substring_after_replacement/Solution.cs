// LeetCode 2301 - Match Substring After Replacement
// https://leetcode.com/problems/match-substring-after-replacement/

using System.Collections.Generic;

public class Solution {
    public bool MatchReplacement(string s, string sub, char[][] mappings) {
        var allow = new HashSet<int>();
        foreach (var m in mappings) allow.Add((m[0] << 8) | m[1]);
        int n = s.Length, mlen = sub.Length;
        for (int i = 0; i + mlen <= n; i++) {
            bool ok = true;
            for (int j = 0; j < mlen; j++) {
                char a = s[i + j], b = sub[j];
                if (a == b || allow.Contains((b << 8) | a)) continue;
                ok = false;
                break;
            }
            if (ok) return true;
        }
        return false;
    }
}
