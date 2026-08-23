// LeetCode 3138 - Minimum Length of Anagram Concatenation
// https://leetcode.com/problems/minimum-length-of-anagram-concatenation/

public class Solution {
    public int MinAnagramLength(string s) {
        int n = s.Length;
        int[] cnt = new int[26];
        foreach (char c in s) cnt[c - 'a']++;
        bool Check(int k) {
            for (int i = 0; i < n; i += k) {
                int[] cnt1 = new int[26];
                for (int j = i; j < i + k; j++) cnt1[s[j] - 'a']++;
                for (int j = 0; j < 26; j++) {
                    if (cnt1[j] * (n / k) != cnt[j]) return false;
                }
            }
            return true;
        }
        for (int i = 1; ; i++) {
            if (n % i == 0 && Check(i)) return i;
        }
    }
}
