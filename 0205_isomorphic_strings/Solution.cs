// LeetCode 0205 - Isomorphic Strings\n// https://leetcode.com/problems/\n\nusing System.Collections.Generic;

public class Solution {
    public bool IsIsomorphic(string s, string t) {
        var forward = new Dictionary<char, char>();
        var backward = new Dictionary<char, char>();
        for (var i = 0; i < s.Length; i++) {
            var a = s[i]; var b = t[i];
            if ((forward.TryGetValue(a, out var mapped) && mapped != b) || (backward.TryGetValue(b, out var reverse) && reverse != a)) return false;
            forward[a] = b; backward[b] = a;
        }
        return true;
    }
}
