// LeetCode 2097 - Valid Arrangement of Pairs
// https://leetcode.com/problems/valid-arrangement-of-pairs/

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
    vector<vector<int>> validArrangement(vector<vector<int>>& pairs) {
        unordered_map<int, vector<int>> g;
        unordered_map<int, int> indeg, outdeg;
        for (auto& p : pairs) {
            int u = p[0], v = p[1];
            g[u].push_back(v);
            outdeg[u]++; indeg[v]++;
        }
        int start = pairs[0][0];
        for (auto& [u, o] : outdeg) if (o - indeg[u] == 1) { start = u; break; }
        vector<int> path;
        function<void(int)> dfs = [&](int u) {
            while (!g[u].empty()) {
                int v = g[u].back(); g[u].pop_back();
                dfs(v);
            }
            path.push_back(u);
        };
        dfs(start);
        reverse(path.begin(), path.end());
        vector<vector<int>> ans;
        for (int i = 0; i + 1 < (int)path.size(); i++) ans.push_back({path[i], path[i + 1]});
        return ans;
    }
};
