// LeetCode 1724 - Checking Existence of Edge Length Limited Paths II
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths-ii/

#include <algorithm>
#include <array>
#include <vector>

class DistanceLimitedPathsExist {
    std::vector<int> weights;
    std::vector<std::vector<int>> versions;

    static int findCompress(std::vector<int>& parent, int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

public:
    DistanceLimitedPathsExist(int n, std::vector<std::vector<int>>& edgeList) {
        std::vector<std::array<int, 3>> edges;
        edges.reserve(edgeList.size());
        for (const std::vector<int>& edge : edgeList) {
            edges.push_back({edge[2], edge[0], edge[1]});
        }
        std::sort(edges.begin(), edges.end());
        std::vector<int> parent(n);
        std::vector<int> size(n, 1);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        size_t i = 0;
        while (i < edges.size()) {
            int weight = edges[i][0];
            while (i < edges.size() && edges[i][0] == weight) {
                int ra = findCompress(parent, edges[i][1]);
                int rb = findCompress(parent, edges[i][2]);
                if (ra != rb) {
                    if (size[ra] < size[rb]) std::swap(ra, rb);
                    parent[rb] = ra;
                    size[ra] += size[rb];
                }
                i++;
            }
            weights.push_back(weight);
            versions.push_back(parent);
        }
    }

    bool query(int p, int q, int limit) {
        int idx = static_cast<int>(
            std::lower_bound(weights.begin(), weights.end(), limit) - weights.begin()) - 1;
        if (idx < 0) return p == q;
        const std::vector<int>& parent = versions[idx];
        int rp = p;
        while (parent[rp] != rp) rp = parent[rp];
        int rq = q;
        while (parent[rq] != rq) rq = parent[rq];
        return rp == rq;
    }
};
