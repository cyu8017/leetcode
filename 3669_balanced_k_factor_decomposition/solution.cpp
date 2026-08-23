// LeetCode 3669 - Balanced K-Factor Decomposition
// https://leetcode.com/problems/balanced-k-factor-decomposition/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
    static constexpr int MX = 100001;
    static std::vector<std::vector<int>> g;
    static bool inited;
    int cur;
    std::vector<int> ans, path;

    static void ensureInit() {
        if (inited) return;
        g.assign(MX, {});
        for (int i = 1; i < MX; i++) {
            for (int j = i; j < MX; j += i) g[j].push_back(i);
        }
        inited = true;
    }

    void dfs(int i, int x, int mi, int mx) {
        if (i == 0) {
            int d = std::max(mx, x) - std::min(mi, x);
            if (d < cur) {
                cur = d;
                path[i] = x;
                ans = path;
            }
            return;
        }
        for (int y : g[x]) {
            path[i] = y;
            dfs(i - 1, x / y, std::min(mi, y), std::max(mx, y));
        }
    }

public:
    std::vector<int> minDifference(int n, int k) {
        ensureInit();
        cur = INT_MAX;
        ans.clear();
        path.assign(k, 0);
        dfs(k - 1, n, INT_MAX, 0);
        return ans;
    }
};

std::vector<std::vector<int>> Solution::g;
bool Solution::inited = false;
