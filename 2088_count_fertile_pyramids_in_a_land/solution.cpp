// LeetCode 2088 - Count Fertile Pyramids in a Land
// https://leetcode.com/problems/count-fertile-pyramids-in-a-land/

#include <algorithm>
#include <array>
#include <bitset>
#include <cmath>
#include <cstdint>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

class Solution {
    int count(vector<vector<int>> g) {
        int m = (int)g.size(), n = (int)g[0].size();
        vector<vector<int>> dp = g;
        int ans = 0;
        for (int i = m - 2; i >= 0; i--) {
            for (int j = 1; j < n - 1; j++) {
                if (g[i][j] == 1) {
                    dp[i][j] = 1 + min({dp[i + 1][j - 1], dp[i + 1][j], dp[i + 1][j + 1]});
                    ans += dp[i][j] - 1;
                }
            }
        }
        return ans;
    }
public:
    int countPyramids(vector<vector<int>>& grid) {
        int ans = count(grid);
        int m = (int)grid.size();
        vector<vector<int>> rev(m);
        for (int i = 0; i < m; i++) rev[i] = grid[m - 1 - i];
        return ans + count(rev);
    }
};
