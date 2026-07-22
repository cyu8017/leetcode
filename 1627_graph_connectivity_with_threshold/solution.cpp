// LeetCode 1627 - Graph Connectivity With Threshold
// https://leetcode.com/problems/graph-connectivity-with-threshold/

#include <numeric>
#include <vector>

class Solution {
    int find(std::vector<int>& parent, int x) {
        while (x != parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

public:
    std::vector<bool> areConnected(int n, int threshold, std::vector<std::vector<int>>& queries) {
        std::vector<int> parent(n + 1);
        std::iota(parent.begin(), parent.end(), 0);
        for (int d = threshold + 1; d <= n; ++d) {
            for (int x = 2 * d; x <= n; x += d) {
                const int a = find(parent, d);
                const int b = find(parent, x);
                if (a != b) {
                    parent[b] = a;
                }
            }
        }
        std::vector<bool> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            ans.push_back(find(parent, q[0]) == find(parent, q[1]));
        }
        return ans;
    }
};
