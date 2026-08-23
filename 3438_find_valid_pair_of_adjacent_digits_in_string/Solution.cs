// LeetCode 3438 - Find Valid Pair of Adjacent Digits in String
// https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/

public class Solution {
    public string FindValidPair(string s) {
        int[] freq = new int[10];
        foreach (char c in s) freq[c - '0']++;
        for (int i = 0; i + 1 < s.Length; i++) {
            int a = s[i] - '0', b = s[i + 1] - '0';
            if (a != b && freq[a] == a && freq[b] == b) return s.Substring(i, 2);
        }
        return "";
    }
}
