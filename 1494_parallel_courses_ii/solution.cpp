#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minNumberOfSemesters(int n, std::vector<std::vector<int>>& relations, int k) {
        std::vector<int> prereq(n, 0);
        for (auto& e : relations) prereq[e[1] - 1] |= 1 << (e[0] - 1);
        int full = (1 << n) - 1;
        const int inf = 1e9;
        std::vector<int> dp(1 << n, inf);
        dp[0] = 0;
        for (int mask = 0; mask < (1 << n); ++mask) {
            if (dp[mask] == inf) continue;
            int available = 0;
            for (int c = 0; c < n; ++c)
                if (((mask >> c) & 1) == 0 && (prereq[c] & mask) == prereq[c])
                    available |= 1 << c;
            std::vector<int> choices;
            if (__builtin_popcount(available) <= k) choices.push_back(available);
            else {
                for (int sub = available; sub; sub = (sub - 1) & available)
                    if (__builtin_popcount(sub) == k) choices.push_back(sub);
            }
            for (int take : choices)
                dp[mask | take] = std::min(dp[mask | take], dp[mask] + 1);
        }
        return dp[full];
    }
};
