// LeetCode 2186 - Minimum Number of Steps to Make Two Strings Anagram II
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

public class Solution {
    public int MinSteps(string s, string t) {
        int[] freq = new int[26];
        foreach (char c in s) freq[c - 'a']++;
        foreach (char c in t) freq[c - 'a']--;
        int ans = 0;
        foreach (int v in freq) ans += Math.Abs(v);
        return ans;
    }
}
