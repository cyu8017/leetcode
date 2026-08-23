// LeetCode 3098 - Find the Sum of Subsequence Powers
// https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

#include <algorithm>
#include <climits>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int sumOfPowers(std::vector<int>& nums, int k) {
        const int mod = 1e9 + 7;
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        std::unordered_map<long long, int> f;
        auto dfs = [&](auto&& self, int i, int j, int kk, int mi) -> int {
            if (i >= n) return kk == 0 ? mi : 0;
            if (n - i < kk) return 0;
            long long key = ((long long)mi << 18) | ((long long)i << 12) | ((long long)j << 6) | kk;
            if (f.count(key)) return f[key];
            int ans = self(self, i + 1, j, kk, mi);
            if (j == n) ans = (ans + self(self, i + 1, i, kk - 1, mi)) % mod;
            else ans = (ans + self(self, i + 1, i, kk - 1, std::min(mi, nums[i] - nums[j]))) % mod;
            return f[key] = ans;
        };
        return dfs(dfs, 0, n, k, INT_MAX);
    }
};
