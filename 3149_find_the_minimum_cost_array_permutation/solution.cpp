// LeetCode 3149 - Find the Minimum Cost Array Permutation
// https://leetcode.com/problems/find-the-minimum-cost-array-permutation/

#include <vector>
#include <cstdlib>
#include <climits>

class Solution {
public:
    std::vector<int> findPermutation(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<std::vector<int>> memo(1 << n, std::vector<int>(n, -1));
        auto absv = [](int x) { return x < 0 ? -x : x; };
        auto dfs = [&](auto&& self, int mask, int pre) -> int {
            if (mask == (1 << n) - 1) return absv(pre - nums[0]);
            if (memo[mask][pre] != -1) return memo[mask][pre];
            int res = INT_MAX;
            for (int cur = 1; cur < n; cur++) {
                if (((mask >> cur) & 1) == 0) {
                    res = std::min(res, absv(pre - nums[cur]) + self(self, mask | (1 << cur), cur));
                }
            }
            return memo[mask][pre] = res;
        };
        std::vector<int> ans;
        auto g = [&](auto&& self, int mask, int pre) -> void {
            ans.push_back(pre);
            if (mask == (1 << n) - 1) return;
            int res = dfs(dfs, mask, pre);
            for (int cur = 1; cur < n; cur++) {
                if (((mask >> cur) & 1) == 0) {
                    if (absv(pre - nums[cur]) + dfs(dfs, mask | (1 << cur), cur) == res) {
                        self(self, mask | (1 << cur), cur);
                        break;
                    }
                }
            }
        };
        g(g, 1, 0);
        return ans;
    }
};
