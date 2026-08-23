// LeetCode 0809 - Expressive Words
// https://leetcode.com/problems/expressive-words/

using System.Collections.Generic;

public class Solution {
    public int ExpressiveWords(string s, string[] words) {
        List<(char ch, int cnt)> Groups(string text) {
            var result = new List<(char, int)>();
            int i = 0, n = text.Length;
            while (i < n) {
                int j = i;
                while (j < n && text[j] == text[i]) j++;
                result.Add((text[i], j - i));
                i = j;
            }
            return result;
        }
        var target = Groups(s);
        int ans = 0;
        foreach (string word in words) {
            var source = Groups(word);
            if (source.Count != target.Count) continue;
            bool ok = true;
            for (int i = 0; i < source.Count; i++) {
                if (source[i].ch != target[i].ch) { ok = false; break; }
                int c1 = source[i].cnt, c2 = target[i].cnt;
                if (c1 > c2 || (c1 != c2 && c2 < 3)) { ok = false; break; }
            }
            if (ok) ans++;
        }
        return ans;
    }
}
