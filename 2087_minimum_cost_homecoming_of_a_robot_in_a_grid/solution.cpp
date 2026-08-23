// LeetCode 2087 - Minimum Cost Homecoming of a Robot in a Grid
// https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/

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
    int minCost(vector<int>& startPos, vector<int>& homePos, vector<int>& rowCosts, vector<int>& colCosts) {
        int ans = 0;
        int sr = startPos[0], sc = startPos[1], hr = homePos[0], hc = homePos[1];
        if (sr < hr) for (int r = sr + 1; r <= hr; r++) ans += rowCosts[r];
        else for (int r = sr - 1; r >= hr; r--) ans += rowCosts[r];
        if (sc < hc) for (int c = sc + 1; c <= hc; c++) ans += colCosts[c];
        else for (int c = sc - 1; c >= hc; c--) ans += colCosts[c];
        return ans;
    }
};
