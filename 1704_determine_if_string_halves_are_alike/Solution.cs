// LeetCode 1704 - Determine if String Halves Are Alike
// https://leetcode.com/problems/determine-if-string-halves-are-alike/

public class Solution {
    public bool HalvesAreAlike(string s) {
        const string vowels = "aeiouAEIOU";
        int mid = s.Length / 2;
        int balance = 0;
        for (int i = 0; i < s.Length; i++) {
            if (vowels.IndexOf(s[i]) >= 0) {
                balance += i < mid ? 1 : -1;
            }
        }
        return balance == 0;
    }
}
