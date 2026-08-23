// LeetCode 2033 - Minimum Operations to Make a Uni-Value Grid
// https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

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
    int minOperations(vector<vector<int>>& grid, int x) {
        vector<int> vals;
        int base = grid[0][0] % x;
        for (auto& row : grid) for (int v : row) {
            if (v % x != base) return -1;
            vals.push_back(v);
        }
        sort(vals.begin(), vals.end());
        int median = vals[vals.size() / 2], ans = 0;
        for (int v : vals) ans += abs(v - median) / x;
        return ans;
    }
};
