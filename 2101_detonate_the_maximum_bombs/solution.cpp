// LeetCode 2101 - Detonate the Maximum Bombs
// https://leetcode.com/problems/detonate-the-maximum-bombs/

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
    int maximumDetonation(vector<vector<int>>& bombs) {
        int n = (int)bombs.size();
        vector<vector<int>> g(n);
        for (int i = 0; i < n; i++) {
            long long x1 = bombs[i][0], y1 = bombs[i][1], r1 = bombs[i][2];
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                long long dx = bombs[j][0] - x1, dy = bombs[j][1] - y1;
                if (dx * dx + dy * dy <= r1 * r1) g[i].push_back(j);
            }
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            vector<char> vis(n);
            queue<int> q;
            q.push(i); vis[i] = 1;
            int cnt = 0;
            while (!q.empty()) {
                int u = q.front(); q.pop();
                cnt++;
                for (int v : g[u]) if (!vis[v]) { vis[v] = 1; q.push(v); }
            }
            ans = max(ans, cnt);
        }
        return ans;
    }
};
