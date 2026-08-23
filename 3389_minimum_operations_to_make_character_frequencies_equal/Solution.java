// LeetCode 3389 - Minimum Operations to Make Character Frequencies Equal
// https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/

class Solution {
    public int makeStringGood(String s) {
        int[] freq = new int[26];
        for (char c : s.toCharArray()) freq[c - 'a']++;
        int ans = s.length();
        for (int t = 1; t <= s.length(); t++) {
            int pool = 0;
            for (int i = 0; i < 26; i++) if (freq[i] > t) pool += freq[i] - t;
            int deficit = 0;
            for (int i = 0; i < 26; i++) if (freq[i] < t) deficit += t - freq[i];
            int ops = Math.max(pool, deficit);
            if (ops < ans) ans = ops;
        }
        if (s.length() < ans) ans = s.length();
        return ans;
    }
}
