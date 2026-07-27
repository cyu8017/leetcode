// LeetCode 1647 - Minimum Deletions to Make Character Frequencies Unique
// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

import java.util.*;

class Solution {
    public int minDeletions(String s) {
        int[] freq = new int[26];
        for (char c : s.toCharArray()) freq[c - 'a']++;
        Set<Integer> used = new HashSet<>();
        int ans = 0;
        for (int x : freq) {
            while (x > 0 && used.contains(x)) {
                x--;
                ans++;
            }
            if (x > 0) used.add(x);
        }
        return ans;
    }
}
