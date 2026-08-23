// LeetCode 3129 - Find All Possible Stable Binary Arrays I
// https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/

#include <vector>
#include <array>

class Solution {
public:
    int numberOfStableArrays(int zero, int one, int limit) {
        const int mod = 1e9 + 7;
        std::vector<std::vector<std::array<int, 2>>> f(zero + 1, std::vector<std::array<int, 2>>(one + 1, {-1, -1}));
        auto dfs = [&](auto&& self, int i, int j, int k) -> int {
            if (i < 0 || j < 0) return 0;
            if (i == 0) return (k == 1 && j <= limit) ? 1 : 0;
            if (j == 0) return (k == 0 && i <= limit) ? 1 : 0;
            int& res = f[i][j][k];
            if (res != -1) return res;
            if (k == 0)
                res = (self(self, i - 1, j, 0) + self(self, i - 1, j, 1) - self(self, i - limit - 1, j, 1) + mod) % mod;
            else
                res = (self(self, i, j - 1, 0) + self(self, i, j - 1, 1) - self(self, i, j - limit - 1, 0) + mod) % mod;
            return res;
        };
        return (dfs(dfs, zero, one, 0) + dfs(dfs, zero, one, 1)) % mod;
    }
};
