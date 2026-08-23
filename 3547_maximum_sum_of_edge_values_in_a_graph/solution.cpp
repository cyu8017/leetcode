// LeetCode 3547 - Maximum Sum of Edge Values in a Graph
// https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/

#include <vector>
#include <algorithm>

class Solution {
    long long calc(int left, int right, bool isCycle) {
        int w0 = right, w1 = right;
        long long score = 0;
        for (int value = right - 1; value >= left; value--) {
            score += 1LL * w0 * value;
            w0 = w1;
            w1 = value;
        }
        if (isCycle) score += 1LL * w0 * w1;
        return score;
    }
public:
    long long maxScore(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<int>> graph(n);
        for (auto& e : edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }
        std::vector<char> seen(n);
        std::vector<int> cycleSizes, pathSizes;
        auto getComp = [&](int start) {
            std::vector<int> comp = {start};
            seen[start] = 1;
            for (int i = 0; i < (int)comp.size(); i++) {
                for (int v : graph[comp[i]]) {
                    if (!seen[v]) { seen[v] = 1; comp.push_back(v); }
                }
            }
            return comp;
        };
        for (int i = 0; i < n; i++) {
            if (seen[i]) continue;
            auto comp = getComp(i);
            bool allDeg2 = true;
            for (int u : comp) if ((int)graph[u].size() != 2) { allDeg2 = false; break; }
            if (allDeg2) cycleSizes.push_back((int)comp.size());
            else if ((int)comp.size() > 1) pathSizes.push_back((int)comp.size());
        }
        long long ans = 0;
        int curN = n;
        for (int cs : cycleSizes) {
            ans += calc(curN - cs + 1, curN, true);
            curN -= cs;
        }
        std::sort(pathSizes.rbegin(), pathSizes.rend());
        for (int ps : pathSizes) {
            ans += calc(curN - ps + 1, curN, false);
            curN -= ps;
        }
        return ans;
    }
};
