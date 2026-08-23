// LeetCode 2209 - Minimum White Tiles After Covering With Carpets
// https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/

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
public:
    int minimumWhiteTiles(string floor, int numCarpets, int carpetLen) {
        int n = floor.size();
        vector<vector<int>> dp(numCarpets + 1, vector<int>(n + 1, 1 << 30));
        dp[0][0] = 0;
        for (int j = 1; j <= n; j++) {
            dp[0][j] = dp[0][j - 1] + (floor[j - 1] == '1');
        }
        for (int c = 1; c <= numCarpets; c++) {
            dp[c][0] = 0;
            for (int j = 1; j <= n; j++) {
                dp[c][j] = dp[c][j - 1] + (floor[j - 1] == '1');
                int start = max(0, j - carpetLen);
                dp[c][j] = min(dp[c][j], dp[c - 1][start]);
            }
        }
        return dp[numCarpets][n];
    }
};
