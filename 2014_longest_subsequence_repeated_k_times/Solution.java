// LeetCode 2014 - Longest Subsequence Repeated K Times
// https://leetcode.com/problems/longest-subsequence-repeated-k-times/

import java.util.*;

class Solution {
    public String longestSubsequenceRepeatedK(String s, int k) {
        int[] freq = new int[26];
        for (char c : s.toCharArray()) freq[c - 'a']++;
        StringBuilder chars = new StringBuilder();
        for (int c = 25; c >= 0; c--) if (freq[c] >= k) chars.append((char) ('a' + c));
        String best = "";
        ArrayDeque<String> q = new ArrayDeque<>();
        q.offer("");
        while (!q.isEmpty()) {
            String cur = q.poll();
            for (int i = 0; i < chars.length(); i++) {
                String nxt = cur + chars.charAt(i);
                if (isSubseq(s, nxt, k)) {
                    if (nxt.length() > best.length() || (nxt.length() == best.length() && nxt.compareTo(best) > 0))
                        best = nxt;
                    q.offer(nxt);
                }
            }
        }
        return best;
    }

    private boolean isSubseq(String s, String t, int k) {
        int need = 0, times = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == t.charAt(need)) {
                need++;
                if (need == t.length()) {
                    times++;
                    if (times == k) return true;
                    need = 0;
                }
            }
        }
        return false;
    }
}
