// LeetCode 2203 - Minimum Weighted Subgraph With the Required Paths
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

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
    vector<long long> dijkstra(int n, vector<vector<pair<int,int>>>& g, int src) {
        const long long INF = 1LL << 62;
        vector<long long> dist(n, INF);
        dist[src] = 0;
        priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<>> pq;
        pq.push({0, src});
        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (d != dist[u]) continue;
            for (auto& [v, w] : g[u]) {
                if (d + w < dist[v]) {
                    dist[v] = d + w;
                    pq.push({dist[v], v});
                }
            }
        }
        return dist;
    }
public:
    long long minimumWeight(int n, vector<vector<int>>& edges, int src1, int src2, int dest) {
        vector<vector<pair<int,int>>> g(n), rg(n);
        for (auto& e : edges) {
            g[e[0]].push_back({e[1], e[2]});
            rg[e[1]].push_back({e[0], e[2]});
        }
        auto d1 = dijkstra(n, g, src1);
        auto d2 = dijkstra(n, g, src2);
        auto dd = dijkstra(n, rg, dest);
        const long long INF = 1LL << 62;
        long long ans = INF;
        for (int i = 0; i < n; i++) {
            if (d1[i] >= INF || d2[i] >= INF || dd[i] >= INF) continue;
            ans = min(ans, d1[i] + d2[i] + dd[i]);
        }
        return ans >= INF ? -1 : ans;
    }
};
