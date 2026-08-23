// LeetCode 3973 - Distinct Gate Paths to LCA
// https://leetcode.com/problems/distinct-gate-paths-to-lca/

#include <array>
#include <vector>

class Solution {
    using Mat = std::array<std::array<long long, 2>, 2>;
    static constexpr long long MOD = 1000000007;

    static Mat multiply(const Mat& a, const Mat& b) {
        Mat c{};
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                for (int k = 0; k < 2; k++) {
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD;
                }
            }
        }
        return c;
    }

public:
    int gatePathXor(int n, std::vector<int>& parent, std::vector<std::vector<int>>& gates, std::vector<std::vector<int>>& queries) {
        int logn = 1;
        while ((1 << logn) <= n) logn++;
        std::vector<std::vector<int>> up(logn, std::vector<int>(n));
        std::vector<std::vector<Mat>> product(logn, std::vector<Mat>(n));
        std::vector<std::vector<int>> children(n);
        for (int node = 1; node < n; node++) children[parent[node]].push_back(node);
        std::vector<int> depth(n, 0);
        std::vector<int> order = {0};
        for (int i = 0; i < (int)order.size(); i++) {
            int u = order[i];
            for (int v : children[u]) {
                depth[v] = depth[u] + 1;
                order.push_back(v);
            }
        }
        for (int u = 0; u < n; u++) {
            up[0][u] = (u == 0) ? 0 : parent[u];
            product[0][u] = Mat{{
                {(long long)gates[u][1], (long long)gates[u][2]},
                {(long long)gates[u][2], (long long)gates[u][0]}
            }};
        }
        for (int level = 1; level < logn; level++) {
            for (int u = 0; u < n; u++) {
                int mid = up[level - 1][u];
                up[level][u] = up[level - 1][mid];
                product[level][u] = multiply(product[level - 1][u], product[level - 1][mid]);
            }
        }
        auto liftNode = [&](int node, int distance) {
            for (int level = 0; distance > 0; level++) {
                if (distance & 1) node = up[level][node];
                distance >>= 1;
            }
            return node;
        };
        auto lca = [&](int a, int b) {
            if (depth[a] > depth[b]) a = liftNode(a, depth[a] - depth[b]);
            else if (depth[b] > depth[a]) b = liftNode(b, depth[b] - depth[a]);
            if (a == b) return a;
            for (int level = logn - 1; level >= 0; level--) {
                if (up[level][a] != up[level][b]) {
                    a = up[level][a];
                    b = up[level][b];
                }
            }
            return up[0][a];
        };
        auto ways = [&](int node, int card, int distance) {
            std::array<long long, 2> vector{};
            vector[card] = 1;
            for (int level = 0; distance > 0; level++) {
                if (distance & 1) {
                    Mat matrix = product[level][node];
                    vector = {
                        (vector[0] * matrix[0][0] + vector[1] * matrix[1][0]) % MOD,
                        (vector[0] * matrix[0][1] + vector[1] * matrix[1][1]) % MOD
                    };
                    node = up[level][node];
                }
                distance >>= 1;
            }
            return (vector[0] + vector[1]) % MOD;
        };
        int answer = 0;
        for (auto& query : queries) {
            int ancestor = lca(query[0], query[2]);
            long long alice = ways(query[0], query[1], depth[query[0]] - depth[ancestor]);
            long long bob = ways(query[2], query[3], depth[query[2]] - depth[ancestor]);
            int total = (int)(alice * bob % MOD);
            answer ^= total;
        }
        return answer;
    }
};
