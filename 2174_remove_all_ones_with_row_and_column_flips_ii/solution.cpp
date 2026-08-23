// LeetCode 2174 - Remove All Ones With Row and Column Flips II
// https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii/

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
    int removeOnes(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<pair<int,int>> ones;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == 1) ones.push_back({i, j});
        if (ones.empty()) return 0;
        int ans = m + n;
        function<void(int,int)> dfs = [&](int idx, int flips) {
            if (flips >= ans) return;
            while (idx < (int)ones.size() && grid[ones[idx].first][ones[idx].second] == 0) idx++;
            if (idx == (int)ones.size()) { ans = flips; return; }
            int r = ones[idx].first, c = ones[idx].second;
            vector<pair<int,int>> changed;
            for (int j = 0; j < n; j++) if (grid[r][j] == 1) { grid[r][j] = 0; changed.push_back({r, j}); }
            dfs(idx + 1, flips + 1);
            for (auto& p : changed) grid[p.first][p.second] = 1;
            changed.clear();
            for (int i = 0; i < m; i++) if (grid[i][c] == 1) { grid[i][c] = 0; changed.push_back({i, c}); }
            dfs(idx + 1, flips + 1);
            for (auto& p : changed) grid[p.first][p.second] = 1;
        };
        dfs(0, 0);
        return ans;
    }
};
