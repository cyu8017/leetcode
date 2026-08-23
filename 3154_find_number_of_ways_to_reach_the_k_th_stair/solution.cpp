// LeetCode 3154 - Find Number of Ways to Reach the K-th Stair
// https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/

#include <unordered_map>

class Solution {
public:
    int waysToReachStair(int k) {
        std::unordered_map<long long, int> f;
        auto dfs = [&](auto&& self, long long i, int j, int jump) -> int {
            if (i > k + 1) return 0;
            long long key = (i << 32) | ((long long)jump << 1) | j;
            auto it = f.find(key);
            if (it != f.end()) return it->second;
            int ans = 0;
            if (i == k) ans++;
            if (i > 0 && j == 0) ans += self(self, i - 1, 1, jump);
            ans += self(self, i + (1LL << jump), 0, jump + 1);
            return f[key] = ans;
        };
        return dfs(dfs, 1, 0, 0);
    }
};
