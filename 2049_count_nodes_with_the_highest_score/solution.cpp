// LeetCode 2049 - Count Nodes With the Highest Score
// https://leetcode.com/problems/count-nodes-with-the-highest-score/

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
    int countHighestScoreNodes(vector<int>& parents) {
        int n = (int)parents.size();
        vector<vector<int>> children(n);
        for (int i = 1; i < n; i++) children[parents[i]].push_back(i);
        vector<int> size(n);
        function<int(int)> dfs = [&](int u) {
            size[u] = 1;
            for (int v : children[u]) size[u] += dfs(v);
            return size[u];
        };
        dfs(0);
        long long best = 0;
        int ans = 0;
        for (int u = 0; u < n; u++) {
            long long score = 1;
            for (int v : children[u]) score *= size[v];
            int up = n - size[u];
            if (up > 0) score *= up;
            if (score > best) { best = score; ans = 1; }
            else if (score == best) ans++;
        }
        return ans;
    }
};
