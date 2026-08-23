// LeetCode 2900 - Longest Unequal Adjacent Groups Subsequence I
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> getLongestSubsequence(String[] words, int[] groups) {
        List<String> ans = new ArrayList<>();
        ans.add(words[0]);
        int last = groups[0];
        for (int i = 1; i < words.length; i++) {
            if (groups[i] != last) {
                ans.add(words[i]);
                last = groups[i];
            }
        }
        return ans;
    }
}
