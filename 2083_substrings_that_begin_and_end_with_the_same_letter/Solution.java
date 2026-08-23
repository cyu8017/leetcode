// LeetCode 2083 - Substrings That Begin and End With the Same Letter
// https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/

class Solution {
    public long numberOfSubstrings(String s) {
        long[] freq = new long[26];
        long ans = 0;
        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
            ans += freq[c - 'a'];
        }
        return ans;
    }
}
