// LeetCode 3858 - Minimum Bitwise Or From Grid
// https://leetcode.com/problems/minimum-bitwise-or-from-grid/

#include <algorithm>
#include <vector>

class Solution {
    static int bitLen(unsigned x) {
        return x == 0 ? 0 : 32 - __builtin_clz(x);
    }

public:
    int minimumOR(std::vector<std::vector<int>>& grid) {
        int mx = 0;
        for (auto& row : grid) mx = std::max(mx, *std::max_element(row.begin(), row.end()));
        int m = bitLen((unsigned)mx);
        int ans = 0;
        for (int i = m - 1; i >= 0; i--) {
            int mask = ans | ((1 << i) - 1);
            for (auto& row : grid) {
                bool found = false;
                for (int x : row) {
                    if ((x | mask) == mask) {
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    ans |= 1 << i;
                    break;
                }
            }
        }
        return ans;
    }
};
