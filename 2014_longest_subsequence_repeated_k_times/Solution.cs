// LeetCode 2014 - Longest Subsequence Repeated K Times
// https://leetcode.com/problems/longest-subsequence-repeated-k-times/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string LongestSubsequenceRepeatedK(string s, int k) {
        int[] freq = new int[26];
        foreach (char c in s) freq[c - 'a']++;
        var chars = new StringBuilder();
        for (int c = 25; c >= 0; c--) if (freq[c] >= k) chars.Append((char)('a' + c));
        bool IsSubseq(string t) {
            int need = 0, times = 0;
            foreach (char c in s) {
                if (c == t[need]) {
                    need++;
                    if (need == t.Length) {
                        times++;
                        if (times == k) return true;
                        need = 0;
                    }
                }
            }
            return false;
        }
        string best = "";
        var q = new Queue<string>();
        q.Enqueue("");
        while (q.Count > 0) {
            string cur = q.Dequeue();
            foreach (char ch in chars.ToString()) {
                string nxt = cur + ch;
                if (IsSubseq(nxt)) {
                    if (nxt.Length > best.Length || (nxt.Length == best.Length && string.CompareOrdinal(nxt, best) > 0))
                        best = nxt;
                    q.Enqueue(nxt);
                }
            }
        }
        return best;
    }
}
