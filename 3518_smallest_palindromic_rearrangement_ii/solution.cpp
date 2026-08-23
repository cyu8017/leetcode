// LeetCode 3518 - Smallest Palindromic Rearrangement II
// https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

#include <string>
#include <vector>

class Solution {
    static const int MAX = 1000001;
    int nCk(int n, int kk) {
        if (kk < 0 || kk > n) return 0;
        long long res = 1;
        if (kk > n - kk) kk = n - kk;
        for (int i = 1; i <= kk; i++) {
            res = res * (n - i + 1) / i;
            if (res >= MAX) return MAX;
        }
        return (int)res;
    }
    int countArr(std::vector<int>& h) {
        int total = 0;
        for (int f : h) total += f;
        long long res = 1;
        for (int f : h) {
            res *= nCk(total, f);
            if (res >= MAX) return MAX;
            total -= f;
        }
        return (int)res;
    }
public:
    std::string smallestPalindrome(std::string s, int k) {
        std::vector<int> cnt(26);
        for (char c : s) cnt[c - 'a']++;
        int odd = 0;
        for (int c : cnt) if (c % 2) odd++;
        if (odd > 1) return "";
        std::vector<int> half(26);
        char mid = 0;
        for (int i = 0; i < 26; i++) {
            half[i] = cnt[i] / 2;
            if (cnt[i] % 2) mid = char('a' + i);
        }
        if (countArr(half) < k) return "";
        int halfLen = 0;
        for (int f : half) halfLen += f;
        std::string left;
        for (int t = 0; t < halfLen; t++) {
            for (int i = 0; i < 26; i++) {
                if (half[i] == 0) continue;
                half[i]--;
                int arr = countArr(half);
                if (arr >= k) {
                    left.push_back(char('a' + i));
                    break;
                }
                k -= arr;
                half[i]++;
            }
        }
        std::string res = left;
        if (mid) res.push_back(mid);
        for (int i = (int)left.size() - 1; i >= 0; i--) res.push_back(left[i]);
        return res;
    }
};
