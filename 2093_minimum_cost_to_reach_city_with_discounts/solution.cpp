// LeetCode 2093 - Minimum Cost to Reach City With Discounts
// https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/

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
    int minimumCost(int n, vector<vector<int>>& highways, int discounts) {
        vector<vector<pair<int,int>>> g(n);
        for (auto& h : highways) {
            g[h[0]].push_back({h[1], h[2]});
            g[h[1]].push_back({h[0], h[2]});
        }
        const int INF = 1 << 30;
        vector<vector<int>> dist(n, vector<int>(discounts + 1, INF));
        priority_queue<array<int,3>, vector<array<int,3>>, greater<>> pq;
        dist[0][discounts] = 0;
        pq.push({0, 0, discounts});
        while (!pq.empty()) {
            auto [cost, city, disc] = pq.top(); pq.pop();
            if (city == n - 1) return cost;
            if (cost > dist[city][disc]) continue;
            for (auto [v, w] : g[city]) {
                if (cost + w < dist[v][disc]) {
                    dist[v][disc] = cost + w;
                    pq.push({dist[v][disc], v, disc});
                }
                if (disc > 0 && cost + w / 2 < dist[v][disc - 1]) {
                    dist[v][disc - 1] = cost + w / 2;
                    pq.push({dist[v][disc - 1], v, disc - 1});
                }
            }
        }
        return -1;
    }
};
