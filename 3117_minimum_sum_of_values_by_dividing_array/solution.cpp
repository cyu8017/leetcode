// LeetCode 3117 - Minimum Sum of Values by Dividing Array
// https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

#include <vector>
#include <unordered_map>
#include <algorithm>
#include <climits>

class Solution {
public:
    int minimumValueSum(std::vector<int>& nums, std::vector<int>& andValues) {
        int n = (int)nums.size(), m = (int)andValues.size();
        const int inf = 1 << 29;
        std::unordered_map<long long, int> f;
        auto dfs = [&](auto&& self, int i, int j, int a) -> int {
            if (n - i < m - j) return inf;
            if (j == m) return i == n ? 0 : inf;
            a &= nums[i];
            if (a < andValues[j]) return inf;
            long long key = ((long long)i << 36) | ((long long)j << 32) | (unsigned)a;
            auto it = f.find(key);
            if (it != f.end()) return it->second;
            int ans = self(self, i + 1, j, a);
            if (a == andValues[j]) {
                ans = std::min(ans, self(self, i + 1, j + 1, -1) + nums[i]);
            }
            return f[key] = ans;
        };
        int ans = dfs(dfs, 0, 0, -1);
        return ans < inf ? ans : -1;
    }
};
