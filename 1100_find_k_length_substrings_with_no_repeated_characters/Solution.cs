// LeetCode 1100 - Find K-Length Substrings With No Repeated Characters
// https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

using System.Collections.Generic;

public class Solution {
    public int NumKLenSubstrNoRepeats(string s, int k) {
        if (k > s.Length) {
            return 0;
        }
        var window = new Dictionary<char, int>();
        for (int i = 0; i < k; i++) {
            if (!window.ContainsKey(s[i])) window[s[i]] = 0;
            window[s[i]]++;
        }
        int ans = window.Count == k ? 1 : 0;
        for (int i = k; i < s.Length; i++) {
            if (!window.ContainsKey(s[i])) window[s[i]] = 0;
            window[s[i]]++;
            char left = s[i - k];
            if (--window[left] == 0) {
                window.Remove(left);
            }
            if (window.Count == k) {
                ans++;
            }
        }
        return ans;
    }
}
