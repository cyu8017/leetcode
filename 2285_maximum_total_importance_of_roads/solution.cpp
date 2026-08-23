// LeetCode 2285 - Maximum Total Importance of Roads
// https://leetcode.com/problems/maximum-total-importance-of-roads/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long maximumImportance(int n, std::vector<std::vector<int>>& roads) {
        std::vector<int> deg(n);
        for (auto& r : roads) { deg[r[0]]++; deg[r[1]]++; }
        std::sort(deg.begin(), deg.end());
        long long ans = 0;
        for (int i = 0; i < n; ++i) ans += 1LL * deg[i] * (i + 1);
        return ans;
    }
};
