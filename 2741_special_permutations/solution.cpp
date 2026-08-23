// LeetCode 2741 - Special Permutations
// https://leetcode.com/problems/special-permutations/

#include <vector>
#include <functional>

class Solution {
public:
    int specialPerm(std::vector<int>& nums) {
        const int MOD = 1000000007;
        int n = (int)nums.size();
        std::vector<std::vector<int>> memo(1 << n, std::vector<int>(n, -1));
        std::function<int(int,int)> dfs = [&](int mask, int last) -> int {
            if (mask == (1 << n) - 1) return 1;
            if (memo[mask][last] != -1) return memo[mask][last];
            int res = 0;
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) continue;
                if (nums[i] % nums[last] == 0 || nums[last] % nums[i] == 0)
                    res = (res + dfs(mask | (1 << i), i)) % MOD;
            }
            return memo[mask][last] = res;
        };
        int ans = 0;
        for (int i = 0; i < n; i++) ans = (ans + dfs(1 << i, i)) % MOD;
        return ans;
    }
};
