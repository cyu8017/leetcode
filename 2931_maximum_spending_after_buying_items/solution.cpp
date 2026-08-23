// LeetCode 2931 - Maximum Spending After Buying Items
// https://leetcode.com/problems/maximum-spending-after-buying-items/

#include <vector>

class Solution {
public:
    long long maxSpending(std::vector<std::vector<int>>& values) {
        int m = (int)values.size(), n = (int)values[0].size();
        std::vector<int> idx(m, n - 1);
        long long ans = 0, day = 1;
        int total = m * n;
        for (int t = 0; t < total; t++) {
            int bestI = -1; long long bestV = (1LL << 60);
            for (int i = 0; i < m; i++) {
                if (idx[i] >= 0 && values[i][idx[i]] < bestV) {
                    bestV = values[i][idx[i]];
                    bestI = i;
                }
            }
            ans += 1LL * bestV * day;
            idx[bestI]--;
            day++;
        }
        return ans;
    }
};
