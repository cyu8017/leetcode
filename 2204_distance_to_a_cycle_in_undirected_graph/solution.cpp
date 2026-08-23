// LeetCode 2204 - Distance to a Cycle in Undirected Graph
// https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/

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
    vector<int> distanceToCycle(int n, vector<vector<int>>& edges) {
        vector<vector<int>> g(n);
        vector<int> deg(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
            deg[e[0]]++; deg[e[1]]++;
        }
        queue<int> q;
        for (int i = 0; i < n; i++) if (deg[i] == 1) q.push(i);
        vector<char> onCycle(n, 1);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            onCycle[u] = 0;
            for (int v : g[u]) {
                if (--deg[v] == 1) q.push(v);
            }
        }
        vector<int> ans(n, -1);
        queue<int> qq;
        for (int i = 0; i < n; i++) if (onCycle[i]) { ans[i] = 0; qq.push(i); }
        while (!qq.empty()) {
            int u = qq.front(); qq.pop();
            for (int v : g[u]) if (ans[v] == -1) {
                ans[v] = ans[u] + 1;
                qq.push(v);
            }
        }
        return ans;
    }
};
