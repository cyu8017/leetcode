// LeetCode 2484 - Count Palindromic Subsequences
// https://leetcode.com/problems/count-palindromic-subsequences/

#include <array>
#include <string>
#include <vector>

class Solution {
public:
    int countPalindromes(std::string s) {
        const int mod = 1000000007;
        int n = (int)s.size();
        std::vector<std::array<std::array<int, 10>, 10>> pref(n), suf(n);
        std::array<int, 10> cnt{};
        for (int i = 0; i < n; i++) {
            if (i > 0) pref[i] = pref[i - 1];
            int d = s[i] - '0';
            for (int a = 0; a < 10; a++) pref[i][a][d] += cnt[a];
            cnt[d]++;
        }
        cnt.fill(0);
        for (int i = n - 1; i >= 0; i--) {
            if (i + 1 < n) suf[i] = suf[i + 1];
            int d = s[i] - '0';
            for (int a = 0; a < 10; a++) suf[i][a][d] += cnt[a];
            cnt[d]++;
        }
        int ans = 0;
        for (int i = 2; i < n - 2; i++) {
            for (int a = 0; a < 10; a++) {
                for (int b = 0; b < 10; b++) {
                    ans = (ans + (long long)pref[i - 1][a][b] * suf[i + 1][a][b]) % mod;
                }
            }
        }
        return ans;
    }
};
