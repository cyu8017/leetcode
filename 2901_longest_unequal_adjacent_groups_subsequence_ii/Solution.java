// LeetCode 2901 - Longest Unequal Adjacent Groups Subsequence II
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public List<String> getWordsInLongestSubsequence(String[] words, int[] groups) {
        int n = words.length;
        int[] dp = new int[n], prev = new int[n];
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
            prev[i] = -1;
        }
        int best = 1, bestI = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (groups[i] != groups[j] && hamming(words[i], words[j]) == 1 && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    prev[i] = j;
                }
            }
            if (dp[i] > best) {
                best = dp[i];
                bestI = i;
            }
        }
        List<String> path = new ArrayList<>();
        for (int i = bestI; i != -1; i = prev[i]) path.add(words[i]);
        Collections.reverse(path);
        return path;
    }

    private int hamming(String a, String b) {
        if (a.length() != b.length()) return 100;
        int d = 0;
        for (int i = 0; i < a.length(); i++) if (a.charAt(i) != b.charAt(i)) d++;
        return d;
    }
}
