// LeetCode 0916 - Word Subsets
// https://leetcode.com/problems/word-subsets/

import java.util.*;

class Solution {
    public List<String> wordSubsets(String[] words1, String[] words2) {
        int[] need = new int[26];
        for (String w : words2) {
            int[] cnt = new int[26];
            for (char c : w.toCharArray()) cnt[c - 'a']++;
            for (int i = 0; i < 26; i++) need[i] = Math.max(need[i], cnt[i]);
        }
        List<String> ans = new ArrayList<>();
        for (String w : words1) {
            int[] cnt = new int[26];
            for (char c : w.toCharArray()) cnt[c - 'a']++;
            boolean ok = true;
            for (int i = 0; i < 26; i++) if (cnt[i] < need[i]) { ok = false; break; }
            if (ok) ans.add(w);
        }
        return ans;
    }
}
