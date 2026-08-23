// LeetCode 3186 - Maximum Total Damage With Spell Casting
// https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    long long maximumTotalDamage(std::vector<int>& power) {
        int n = (int)power.size();
        std::sort(power.begin(), power.end());
        std::unordered_map<int, int> cnt;
        std::vector<int> nxt(n);
        std::vector<long long> f(n);
        for (int i = 0; i < n; i++) {
            cnt[power[i]]++;
            nxt[i] = (int)(std::lower_bound(power.begin(), power.end(), power[i] + 3) - power.begin());
        }
        auto dfs = [&](auto&& self, int i) -> long long {
            if (i >= n) return 0;
            if (f[i] != 0) return f[i];
            long long a = self(self, i + cnt[power[i]]);
            long long b = 1LL * power[i] * cnt[power[i]] + self(self, nxt[i]);
            return f[i] = std::max(a, b);
        };
        return dfs(dfs, 0);
    }
};
