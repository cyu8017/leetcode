// LeetCode 2050 - Parallel Courses III
// https://leetcode.com/problems/parallel-courses-iii/

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
    int minimumTime(int n, vector<vector<int>>& relations, vector<int>& time) {
        vector<vector<int>> g(n + 1);
        vector<int> indeg(n + 1), dist(n + 1);
        for (auto& e : relations) { g[e[0]].push_back(e[1]); indeg[e[1]]++; }
        queue<int> q;
        for (int i = 1; i <= n; i++) {
            dist[i] = time[i - 1];
            if (!indeg[i]) q.push(i);
        }
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : g[u]) {
                dist[v] = max(dist[v], dist[u] + time[v - 1]);
                if (--indeg[v] == 0) q.push(v);
            }
        }
        return *max_element(dist.begin() + 1, dist.end());
    }
};
