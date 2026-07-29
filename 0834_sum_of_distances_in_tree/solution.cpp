// LeetCode 0834 - Sum of Distances in Tree
// https://leetcode.com/problems/sum-of-distances-in-tree/

#include <functional>
#include <vector>

class Solution {
public:
    std::vector<int> sumOfDistancesInTree(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<int>> graph(n);
        for (auto& e : edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }
        std::vector<int> count(n, 1), ans(n, 0);

        std::function<void(int, int)> post = [&](int node, int parent) {
            for (int child : graph[node]) {
                if (child == parent) {
                    continue;
                }
                post(child, node);
                count[node] += count[child];
                ans[node] += ans[child] + count[child];
            }
        };
        std::function<void(int, int)> reroot = [&](int node, int parent) {
            for (int child : graph[node]) {
                if (child == parent) {
                    continue;
                }
                ans[child] = ans[node] - count[child] + (n - count[child]);
                reroot(child, node);
            }
        };

        post(0, -1);
        reroot(0, -1);
        return ans;
    }
};
