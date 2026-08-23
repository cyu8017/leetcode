// LeetCode 3700 - Number of ZigZag Arrays II
// https://leetcode.com/problems/number-of-zigzag-arrays-ii/

#include <vector>

class Solution {
public:
    int zigZagArrays(int n, int l, int r) {
        const int MOD = 1000000007;
        int m = r - l + 1;
        if (n == 1) return m % MOD;
        std::vector<int> up(m, 1), down(m, 1);
        for (int length = 2; length <= n; length++) {
            std::vector<int> pref(m + 1, 0);
            for (int j = 0; j < m; j++) pref[j + 1] = (pref[j] + down[j]) % MOD;
            std::vector<int> nup(m);
            for (int j = 0; j < m; j++) nup[j] = pref[j];
            std::vector<int> suf(m + 1, 0);
            for (int j = m - 1; j >= 0; j--) suf[j] = (suf[j + 1] + up[j]) % MOD;
            std::vector<int> ndown(m);
            for (int j = 0; j < m; j++) ndown[j] = suf[j + 1];
            up.swap(nup);
            down.swap(ndown);
        }
        int ans = 0;
        for (int j = 0; j < m; j++) {
            ans = (ans + up[j]) % MOD;
            ans = (ans + down[j]) % MOD;
        }
        return ans;
    }
};
