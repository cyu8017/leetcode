// LeetCode 3470 - Permutations IV
// https://leetcode.com/problems/permutations-iv/

#include <vector>

class Solution {
public:
    std::vector<int> permute(int n, long long k) {
        std::vector<long long> fact(n + 1);
        fact[0] = 1;
        for (int i = 1; i <= n; i++) {
            fact[i] = fact[i - 1] * i;
            if (fact[i] > (long long)1e18) fact[i] = (long long)1e18 + 1;
        }
        std::vector<bool> used(n + 1, false);
        std::vector<int> ans;
        auto dfs = [&](auto&& self, int pos) -> bool {
            if (pos == n) return true;
            for (int x = 1; x <= n; x++) {
                if (used[x]) continue;
                if (pos > 0 && (ans[pos - 1] % 2 == x % 2)) continue;
                int rem = n - pos - 1;
                long long cnt = fact[rem];
                if (cnt >= k) {
                    used[x] = true;
                    ans.push_back(x);
                    if (self(self, pos + 1)) return true;
                    ans.pop_back();
                    used[x] = false;
                } else {
                    k -= cnt;
                }
            }
            return false;
        };
        if (!dfs(dfs, 0)) return {};
        return ans;
    }
};
