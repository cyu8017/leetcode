// LeetCode 2123 - Minimum Operations to Remove Adjacent Ones in Matrix
// https://leetcode.com/problems/minimum-operations-to-remove-adjacent-ones-in-matrix/

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
    int minimumOperations(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> id(m, vector<int>(n, -1));
        int cnt = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == 1) id[i][j] = cnt++;
        vector<vector<int>> g(cnt);
        int dirs[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != 1 || (i + j) % 2 != 0) continue;
                int u = id[i][j];
                for (auto& d : dirs) {
                    int ni = i + d[0], nj = j + d[1];
                    if (ni >= 0 && nj >= 0 && ni < m && nj < n && grid[ni][nj] == 1)
                        g[u].push_back(id[ni][nj]);
                }
            }
        }
        vector<int> match(cnt, -1);
        function<bool(int, vector<char>&)> dfs = [&](int u, vector<char>& seen) -> bool {
            for (int v : g[u]) {
                if (seen[v]) continue;
                seen[v] = 1;
                if (match[v] == -1 || dfs(match[v], seen)) {
                    match[v] = u;
                    return true;
                }
            }
            return false;
        };
        int ans = 0;
        for (int u = 0; u < cnt; u++) {
            bool ok = false;
            for (int i = 0; i < m && !ok; i++)
                for (int j = 0; j < n; j++)
                    if (id[i][j] == u && (i + j) % 2 == 0) { ok = true; break; }
            if (!ok) continue;
            vector<char> seen(cnt);
            if (dfs(u, seen)) ans++;
        }
        return ans;
    }
};
