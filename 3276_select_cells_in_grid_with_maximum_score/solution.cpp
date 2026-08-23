// LeetCode 3276 - Select Cells in Grid With Maximum Score
// https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/

#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int maxScore(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size();
        std::unordered_map<int, std::vector<int>> vals;
        for (int i = 0; i < m; i++) {
            std::unordered_set<int> seen;
            for (int v : grid[i]) {
                if (!seen.count(v)) {
                    vals[v].push_back(i);
                    seen.insert(v);
                }
            }
        }
        std::vector<int> arr;
        for (auto& p : vals) arr.push_back(p.first);
        std::sort(arr.begin(), arr.end(), std::greater<int>());
        int N = 1 << m;
        std::vector<int> dp(N, 0);
        for (int v : arr) {
            std::vector<int> ndp = dp;
            for (int r : vals[v]) {
                int bit = 1 << r;
                for (int mask = 0; mask < N; mask++) {
                    if (mask & bit) continue;
                    int cand = dp[mask] + v;
                    int nmask = mask | bit;
                    if (cand > ndp[nmask]) ndp[nmask] = cand;
                }
            }
            dp = ndp;
        }
        return *std::max_element(dp.begin(), dp.end());
    }
};
