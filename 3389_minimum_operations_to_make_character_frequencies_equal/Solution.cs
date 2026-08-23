// LeetCode 3389 - Minimum Operations to Make Character Frequencies Equal
// https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/

public class Solution {
    public int MakeStringGood(string s) {
        int[] freq = new int[26];
        foreach (char c in s) freq[c - 'a']++;
        int ans = s.Length;
        for (int t = 1; t <= s.Length; t++) {
            int pool = 0;
            for (int i = 0; i < 26; i++) if (freq[i] > t) pool += freq[i] - t;
            int deficit = 0;
            for (int i = 0; i < 26; i++) if (freq[i] < t) deficit += t - freq[i];
            int ops = (pool >= deficit) ? pool : deficit;
            if (ops < ans) ans = ops;
        }
        if (s.Length < ans) ans = s.Length;
        return ans;
    }
}
