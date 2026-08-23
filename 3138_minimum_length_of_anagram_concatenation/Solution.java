// LeetCode 3138 - Minimum Length of Anagram Concatenation
// https://leetcode.com/problems/minimum-length-of-anagram-concatenation/

class Solution {
    public int minAnagramLength(String s) {
        int n = s.length();
        int[] cnt = new int[26];
        for (int i = 0; i < n; i++) cnt[s.charAt(i) - 'a']++;
        for (int i = 1; ; i++) {
            if (n % i == 0 && check(s, n, cnt, i)) return i;
        }
    }

    private boolean check(String s, int n, int[] cnt, int k) {
        for (int i = 0; i < n; i += k) {
            int[] cnt1 = new int[26];
            for (int j = i; j < i + k; j++) cnt1[s.charAt(j) - 'a']++;
            for (int j = 0; j < 26; j++) {
                if (cnt1[j] * (n / k) != cnt[j]) return false;
            }
        }
        return true;
    }
}
