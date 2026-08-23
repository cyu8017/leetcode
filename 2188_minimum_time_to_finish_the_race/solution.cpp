// LeetCode 2188 - Minimum Time to Finish the Race
// https://leetcode.com/problems/minimum-time-to-finish-the-race/

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
    int minimumFinishTime(vector<vector<int>>& tires, int changeTime, int numLaps) {
        vector<int> minTime(20, 1 << 30);
        for (auto& tire : tires) {
            int f = tire[0], r = tire[1];
            long long t = f, lap = f;
            for (int x = 1; x < 20 && t < minTime[x]; x++) {
                minTime[x] = (int)t;
                lap *= r;
                if (lap > changeTime + f) break;
                t += lap;
            }
        }
        vector<int> dp(numLaps + 1, 1 << 30);
        dp[0] = -changeTime;
        for (int i = 1; i <= numLaps; i++)
            for (int j = 1; j <= i && j < 20; j++)
                dp[i] = min(dp[i], dp[i - j] + changeTime + minTime[j]);
        return dp[numLaps];
    }
};
