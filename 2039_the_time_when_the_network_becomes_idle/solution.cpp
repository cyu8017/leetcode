// LeetCode 2039 - The Time When the Network Becomes Idle
// https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

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
    int networkBecomesIdle(vector<vector<int>>& edges, vector<int>& patience) {
        int n = (int)patience.size();
        vector<vector<int>> g(n);
        for (auto& e : edges) { g[e[0]].push_back(e[1]); g[e[1]].push_back(e[0]); }
        vector<int> dist(n, -1);
        queue<int> q;
        q.push(0); dist[0] = 0;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : g[u]) if (dist[v] == -1) { dist[v] = dist[u] + 1; q.push(v); }
        }
        int ans = 0;
        for (int i = 1; i < n; i++) {
            int round = dist[i] * 2;
            int lastSend = (round - 1) / patience[i] * patience[i];
            ans = max(ans, lastSend + round);
        }
        return ans + 1;
    }
};
