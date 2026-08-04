// LeetCode 1400 - Construct K Palindrome Strings
// https://leetcode.com/problems/construct-k-palindrome-strings/

class Solution {
    public boolean canConstruct(String s, int k) {
        if (k > s.length()) return false;
        int[] cnt = new int[26];
        for (char c : s.toCharArray()) cnt[c - 'a']++;
        int odd = 0;
        for (int v : cnt) if (v % 2 == 1) odd++;
        return odd <= k;
    }
}
