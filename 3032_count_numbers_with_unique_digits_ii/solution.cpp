// LeetCode 3032 - Count Numbers With Unique Digits II
// https://leetcode.com/problems/count-numbers-with-unique-digits-ii/

#include <cstring>
#include <string>
#include <vector>

class Solution {
public:
    int numberCount(int a, int b) {
        std::string num = std::to_string(b);
        std::vector<std::vector<int>> f;
        auto reset = [&]() {
            f.assign(num.size(), std::vector<int>(1 << 10, -1));
        };
        reset();
        auto dfs = [&](auto&& self, int pos, int mask, bool limit) -> int {
            if (pos >= (int)num.size()) return mask != 0 ? 1 : 0;
            if (!limit && f[pos][mask] != -1) return f[pos][mask];
            int up = limit ? num[pos] - '0' : 9;
            int ans = 0;
            for (int i = 0; i <= up; i++) {
                if ((mask >> i) & 1) continue;
                int nxt = mask | (1 << i);
                if (mask == 0 && i == 0) nxt = 0;
                ans += self(self, pos + 1, nxt, limit && i == up);
            }
            if (!limit) f[pos][mask] = ans;
            return ans;
        };
        int y = dfs(dfs, 0, 0, true);
        num = std::to_string(a - 1);
        reset();
        int x = dfs(dfs, 0, 0, true);
        return y - x;
    }
};
