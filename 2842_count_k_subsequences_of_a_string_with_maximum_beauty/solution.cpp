// LeetCode 2842 - Count K-Subsequences of a String With Maximum Beauty
// https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int countKSubsequencesWithMaxBeauty(std::string s, int k) {
        const int MOD = 1000000007;
        int freq[26] = {};
        for (char c : s) freq[c - 'a']++;
        std::vector<int> vals;
        for (int f : freq) if (f > 0) vals.push_back(f);
        if ((int)vals.size() < k) return 0;
        std::sort(vals.begin(), vals.end(), std::greater<int>());
        int threshold = vals[k - 1];
        int need = 0, avail = 0;
        long long prod = 1;
        for (int v : vals) {
            if (v > threshold) { prod = prod * v % MOD; need++; }
            else if (v == threshold) avail++;
        }
        int remain = k - need;
        auto modPow = [&](long long a, long long b) {
            long long res = 1;
            a %= MOD;
            while (b > 0) {
                if (b & 1) res = res * a % MOD;
                a = a * a % MOD;
                b >>= 1;
            }
            return res;
        };
        auto comb = [&](int n, int r) {
            if (r < 0 || r > n) return 0LL;
            long long num = 1, den = 1;
            for (int i = 0; i < r; i++) {
                num = num * (n - i) % MOD;
                den = den * (i + 1) % MOD;
            }
            return num * modPow(den, MOD - 2) % MOD;
        };
        prod = prod * comb(avail, remain) % MOD;
        for (int i = 0; i < remain; i++) prod = prod * threshold % MOD;
        return (int)prod;
    }
};
