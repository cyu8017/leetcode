// LeetCode 2192 - All Ancestors of a Node in a Directed Acyclic Graph
// https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

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
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        vector<vector<int>> g(n);
        vector<int> indeg(n);
        for (auto& e : edges) { g[e[0]].push_back(e[1]); indeg[e[1]]++; }
        vector<set<int>> anc(n);
        queue<int> q;
        for (int i = 0; i < n; i++) if (indeg[i] == 0) q.push(i);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : g[u]) {
                anc[v].insert(u);
                anc[v].insert(anc[u].begin(), anc[u].end());
                if (--indeg[v] == 0) q.push(v);
            }
        }
        vector<vector<int>> ans(n);
        for (int i = 0; i < n; i++) ans[i].assign(anc[i].begin(), anc[i].end());
        return ans;
    }
};
