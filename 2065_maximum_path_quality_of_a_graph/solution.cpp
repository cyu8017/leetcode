// LeetCode 2065 - Maximum Path Quality of a Graph
// https://leetcode.com/problems/maximum-path-quality-of-a-graph/

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
    int maximalPathQuality(vector<int>& values, vector<vector<int>>& edges, int maxTime) {
        int n = (int)values.size();
        vector<vector<pair<int,int>>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back({e[1], e[2]});
            g[e[1]].push_back({e[0], e[2]});
        }
        int ans = 0;
        vector<int> vis(n);
        function<void(int,int,int)> dfs = [&](int u, int time, int quality) {
            if (time > maxTime) return;
            bool first = vis[u] == 0;
            if (first) quality += values[u];
            vis[u]++;
            if (u == 0) ans = max(ans, quality);
            for (auto [v, w] : g[u]) dfs(v, time + w, quality);
            vis[u]--;
        };
        dfs(0, 0, 0);
        return ans;
    }
};
