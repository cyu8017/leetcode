// LeetCode 3518 - Smallest Palindromic Rearrangement II
// https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

class Solution {
    final int MAX = 1000001;
    int nCk(int n, int kk) {
        if (kk < 0 || kk > n) return 0;
        long res = 1;
        if (kk > n - kk) kk = n - kk;
        for (int i = 1; i <= kk; i++) {
            res = res * (n - i + 1) / i;
            if (res >= MAX) return MAX;
        }
        return (int)res;
    }
    int countArr(int[] h) {
        int total = 0;
        for (int f : h) total += f;
        long res = 1;
        for (int f : h) {
            res *= nCk(total, f);
            if (res >= MAX) return MAX;
            total -= f;
        }
        return (int)res;
    }
    public String smallestPalindrome(String s, int k) {
        int[] cnt = new int[26];
        for (char c : s.toCharArray()) cnt[c - 'a']++;
        int odd = 0;
        for (int c : cnt) if (c % 2 != 0) odd++;
        if (odd > 1) return "";
        int[] half = new int[26];
        char mid = '\0';
        for (int i = 0; i < 26; i++) {
            half[i] = cnt[i] / 2;
            if (cnt[i] % 2 != 0) mid = (char)('a' + i);
        }
        if (countArr(half) < k) return "";
        int halfLen = 0;
        for (int f : half) halfLen += f;
        var left = new StringBuilder();
        for (int t = 0; t < halfLen; t++) {
            for (int i = 0; i < 26; i++) {
                if (half[i] == 0) continue;
                half[i]--;
                int arr = countArr(half);
                if (arr >= k) {
                    left.append((char)('a' + i));
                    break;
                }
                k -= arr;
                half[i]++;
            }
        }
        var res = new StringBuilder();
        res.append(left);
        if (mid != '\0') res.append(mid);
        for (int i = left.length() - 1; i >= 0; i--) res.append(left.charAt(i));
        return res.toString();
    }
}
