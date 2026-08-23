// LeetCode 2146 - K Highest Ranked Items Within a Price Range
// https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/

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
    vector<vector<int>> highestRankedKItems(vector<vector<int>>& grid, vector<int>& pricing, vector<int>& start, int k) {
        int m = grid.size(), n = grid[0].size();
        int low = pricing[0], high = pricing[1];
        vector<vector<char>> vis(m, vector<char>(n));
        queue<array<int,3>> q;
        q.push({start[0], start[1], 0});
        vis[start[0]][start[1]] = 1;
        vector<array<int,4>> cands;
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!q.empty()) {
            auto [r, c, d] = q.front(); q.pop();
            if (grid[r][c] >= low && grid[r][c] <= high)
                cands.push_back({d, grid[r][c], r, c});
            for (auto& dir : dirs) {
                int nr = r + dir[0], nc = c + dir[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && !vis[nr][nc] && grid[nr][nc] != 0) {
                    vis[nr][nc] = 1;
                    q.push({nr, nc, d + 1});
                }
            }
        }
        sort(cands.begin(), cands.end());
        if (k > (int)cands.size()) k = cands.size();
        vector<vector<int>> ans(k);
        for (int i = 0; i < k; i++) ans[i] = {cands[i][2], cands[i][3]};
        return ans;
    }
};
