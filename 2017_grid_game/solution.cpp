// LeetCode 2017 - Grid Game
// https://leetcode.com/problems/grid-game/

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
    long long gridGame(vector<vector<int>>& grid) {
        int n = (int)grid[0].size();
        long long top = 0, bottom = 0, ans = LLONG_MAX;
        for (int v : grid[0]) top += v;
        for (int i = 0; i < n; i++) {
            top -= grid[0][i];
            ans = min(ans, max(top, bottom));
            bottom += grid[1][i];
        }
        return ans;
    }
};
