// LeetCode 1400 - Construct K Palindrome Strings
// https://leetcode.com/problems/construct-k-palindrome-strings/

public class Solution {
    public bool CanConstruct(string s, int k) {
        var cnt = new int[26];
        foreach (char c in s) cnt[c - 'a']++;
        int odd = 0;
        foreach (int v in cnt) if (v % 2 == 1) odd++;
        return odd <= k && k <= s.Length;
    }
}
