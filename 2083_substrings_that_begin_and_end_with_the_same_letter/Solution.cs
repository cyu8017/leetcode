// LeetCode 2083 - Substrings That Begin and End With the Same Letter
// https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/

public class Solution {
    public long NumberOfSubstrings(string s) {
        long[] freq = new long[26];
        long ans = 0;
        foreach (char c in s) {
            freq[c - 'a']++;
            ans += freq[c - 'a'];
        }
        return ans;
    }
}
