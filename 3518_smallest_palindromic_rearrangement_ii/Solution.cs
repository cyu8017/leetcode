// LeetCode 3518 - Smallest Palindromic Rearrangement II
// https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

using System.Text;

public class Solution {
    const int MAX = 1000001;
    int NCk(int n, int kk) {
        if (kk < 0 || kk > n) return 0;
        long res = 1;
        if (kk > n - kk) kk = n - kk;
        for (int i = 1; i <= kk; i++) {
            res = res * (n - i + 1) / i;
            if (res >= MAX) return MAX;
        }
        return (int)res;
    }
    int CountArr(int[] h) {
        int total = 0;
        foreach (int f in h) total += f;
        long res = 1;
        foreach (int f in h) {
            res *= NCk(total, f);
            if (res >= MAX) return MAX;
            total -= f;
        }
        return (int)res;
    }
    public string SmallestPalindrome(string s, int k) {
        int[] cnt = new int[26];
        foreach (char c in s) cnt[c - 'a']++;
        int odd = 0;
        foreach (int c in cnt) if (c % 2 != 0) odd++;
        if (odd > 1) return "";
        int[] half = new int[26];
        char mid = '\0';
        for (int i = 0; i < 26; i++) {
            half[i] = cnt[i] / 2;
            if (cnt[i] % 2 != 0) mid = (char)('a' + i);
        }
        if (CountArr(half) < k) return "";
        int halfLen = 0;
        foreach (int f in half) halfLen += f;
        var left = new StringBuilder();
        for (int t = 0; t < halfLen; t++) {
            for (int i = 0; i < 26; i++) {
                if (half[i] == 0) continue;
                half[i]--;
                int arr = CountArr(half);
                if (arr >= k) {
                    left.Append((char)('a' + i));
                    break;
                }
                k -= arr;
                half[i]++;
            }
        }
        var res = new StringBuilder();
        res.Append(left);
        if (mid != '\0') res.Append(mid);
        for (int i = left.Length - 1; i >= 0; i--) res.Append(left[i]);
        return res.ToString();
    }
}
