// LeetCode 2127 - Maximum Employees to Be Invited to a Meeting
// https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

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
    int maximumInvitations(vector<int>& favorite) {
        int n = favorite.size();
        vector<int> indeg(n), depth(n, 1);
        for (int f : favorite) indeg[f]++;
        queue<int> q;
        for (int i = 0; i < n; i++) if (indeg[i] == 0) q.push(i);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            int v = favorite[u];
            depth[v] = max(depth[v], depth[u] + 1);
            if (--indeg[v] == 0) q.push(v);
        }
        int pairSum = 0, maxCycle = 0;
        vector<char> vis(n);
        for (int i = 0; i < n; i++) {
            if (indeg[i] == 0 || vis[i]) continue;
            int u = i, lenCycle = 0;
            while (!vis[u]) {
                vis[u] = 1;
                u = favorite[u];
                lenCycle++;
            }
            if (lenCycle == 2) pairSum += depth[i] + depth[favorite[i]];
            else maxCycle = max(maxCycle, lenCycle);
        }
        return max(pairSum, maxCycle);
    }
};
