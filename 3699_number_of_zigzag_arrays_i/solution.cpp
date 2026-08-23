// LeetCode 3699 - Number of ZigZag Arrays I
// https://leetcode.com/problems/number-of-zigzag-arrays-i/

#include <vector>

class Solution {
public:
    int zigZagArrays(int n, int l, int r) {
        const int MOD = 1000000007;
        int m = r - l + 1;
        if (n == 1) return m % MOD;
        std::vector<int> up(m, 1), down(m, 1);
        for (int len_ = 2; len_ <= n; len_++) {
            std::vector<int> prefDown(m + 1, 0);
            for (int j = 0; j < m; j++) prefDown[j + 1] = (prefDown[j] + down[j]) % MOD;
            std::vector<int> nup(m);
            for (int j = 0; j < m; j++) nup[j] = prefDown[j];
            std::vector<int> sufUp(m + 1, 0);
            for (int j = m - 1; j >= 0; j--) sufUp[j] = (sufUp[j + 1] + up[j]) % MOD;
            std::vector<int> ndown(m);
            for (int j = 0; j < m; j++) ndown[j] = sufUp[j + 1];
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
