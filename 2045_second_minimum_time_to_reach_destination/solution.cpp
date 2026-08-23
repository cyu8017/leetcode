// LeetCode 2045 - Second Minimum Time to Reach Destination
// https://leetcode.com/problems/second-minimum-time-to-reach-destination/

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
    int secondMinimum(int n, vector<vector<int>>& edges, int time, int change) {
        vector<vector<int>> g(n + 1);
        for (auto& e : edges) { g[e[0]].push_back(e[1]); g[e[1]].push_back(e[0]); }
        vector<int> dist1(n + 1, -1), dist2(n + 1, -1);
        queue<pair<int,int>> q;
        q.push({1, 0});
        dist1[1] = 0;
        while (!q.empty()) {
            auto [u, d] = q.front(); q.pop();
            for (int v : g[u]) {
                int nd = d + 1;
                if (dist1[v] == -1) { dist1[v] = nd; q.push({v, nd}); }
                else if (dist2[v] == -1 && nd > dist1[v]) { dist2[v] = nd; q.push({v, nd}); }
            }
        }
        int steps = dist2[n], ans = 0;
        for (int i = 0; i < steps; i++) {
            if ((ans / change) % 2 == 1) ans += change - ans % change;
            ans += time;
        }
        return ans;
    }
};
