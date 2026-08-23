// LeetCode 3538 - Merge Operations for Minimum Travel Time
// https://leetcode.com/problems/merge-operations-for-minimum-travel-time/

#include <vector>
#include <map>
#include <array>
#include <algorithm>

class Solution {
public:
    int minTravelTime(int l, int n, int k, std::vector<int>& position, std::vector<int>& time) {
        std::vector<int> prefix(n);
        prefix[0] = time[0];
        for (int i = 1; i < n; i++) prefix[i] = prefix[i - 1] + time[i];
        const long long inf = (long long)1e18;
        std::map<std::array<int, 3>, long long> memo;
        auto dp = [&](auto&& self, int i, int skips, int last) -> long long {
            if (i == n - 1) return skips == 0 ? 0 : inf;
            std::array<int, 3> key = {i, skips, last};
            if (memo.count(key)) return memo[key];
            int rate = prefix[i];
            if (last > 0) rate -= prefix[last - 1];
            long long res = inf;
            int end = n - 1;
            if (i + skips + 1 < end) end = i + skips + 1;
            for (int j = i + 1; j <= end; j++) {
                long long cand = 1LL * (position[j] - position[i]) * rate + self(self, j, skips - (j - i - 1), i + 1);
                if (cand < res) res = cand;
            }
            return memo[key] = res;
        };
        (void)l;
        return (int)dp(dp, 0, k, 0);
    }
};
