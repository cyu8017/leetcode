// LeetCode 0792 - Number of Matching Subsequences
// https://leetcode.com/problems/number-of-matching-subsequences/

import java.util.*;

class Solution {
    public int numMatchingSubseq(String s, String[] words) {
        List<int[]>[] waiting = new List[26];
        for (int i = 0; i < 26; i++) waiting[i] = new ArrayList<>();
        for (int i = 0; i < words.length; i++) {
            String w = words[i];
            waiting[w.charAt(0) - 'a'].add(new int[] {i, 0});
        }
        int ans = 0;
        for (char ch : s.toCharArray()) {
            List<int[]> cur = waiting[ch - 'a'];
            waiting[ch - 'a'] = new ArrayList<>();
            for (int[] it : cur) {
                int wi = it[0], idx = it[1] + 1;
                if (idx == words[wi].length()) ans++;
                else waiting[words[wi].charAt(idx) - 'a'].add(new int[] {wi, idx});
            }
        }
        return ans;
    }
}
