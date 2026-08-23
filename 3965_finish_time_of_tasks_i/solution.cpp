// LeetCode 3965 - Finish Time Of Tasks I
// https://leetcode.com/problems/finish-time-of-tasks-i/

#include <algorithm>
#include <functional>
#include <vector>

class Solution {
public:
    long long finishTime(int n, std::vector<std::vector<int>>& edges, std::vector<int>& baseTime) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) g[e[0]].push_back(e[1]);
        std::function<long long(int)> dfs = [&](int i) -> long long {
            if (g[i].empty()) return baseTime[i];
            const long long INF = 1LL << 62;
            long long earliest = INF, latest = -INF;
            for (int j : g[i]) {
                long long a = dfs(j);
                earliest = std::min(earliest, a);
                latest = std::max(latest, a);
            }
            long long ownDuration = (latest - earliest) + baseTime[i];
            return latest + ownDuration;
        };
        return dfs(0);
    }
};
