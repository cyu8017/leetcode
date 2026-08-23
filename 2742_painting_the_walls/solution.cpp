// LeetCode 2742 - Painting the Walls
// https://leetcode.com/problems/painting-the-walls/

#include <vector>
#include <algorithm>
#include <climits>

class Solution {
public:
    int paintWalls(std::vector<int>& cost, std::vector<int>& time) {
        int n = (int)cost.size();
        const long long INF = (1LL << 60);
        std::vector<long long> dp(n + 1, INF);
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            for (int j = n; j >= 0; j--) {
                int nj = j + time[i] + 1;
                if (nj > n) nj = n;
                if (dp[j] + cost[i] < dp[nj]) dp[nj] = dp[j] + cost[i];
            }
        }
        return (int)dp[n];
    }
};
