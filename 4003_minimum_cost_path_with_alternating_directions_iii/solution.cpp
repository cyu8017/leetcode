// LeetCode 4003 - Minimum Cost Path with Alternating Directions III
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/

#include <cstdint>
#include <functional>
#include <queue>
#include <tuple>
#include <vector>

class Solution {
    static constexpr int64_t INF = (int64_t)1 << 60;

public:
    long long minCost(int m, int n, std::vector<std::vector<int>>& penalty) {
        std::vector<std::vector<std::vector<int64_t>>> dist(
            m, std::vector<std::vector<int64_t>>(n, std::vector<int64_t>(2, INF)));
        dist[0][0][1] = 1;

        using Tup = std::tuple<int64_t, int, int, int>;
        std::priority_queue<Tup, std::vector<Tup>, std::greater<Tup>> pq;
        pq.emplace(1, 0, 0, 1);

        int dirs[4][2] = {{-1, 0}, {0, 1}, {0, -1}, {1, 0}};

        while (!pq.empty()) {
            auto [d, i, j, k] = pq.top();
            pq.pop();
            if (i == m - 1 && j == n - 1) return d;
            if (d > dist[i][j][k]) continue;

            int p = penalty[i][j];
            int64_t nd = d + (int64_t)p;
            if (nd < dist[i][j][k ^ 1]) {
                dist[i][j][k ^ 1] = nd;
                pq.emplace(nd, i, j, k ^ 1);
            }
            for (int idx = 0; idx < 4; idx++) {
                int x = i + dirs[idx][0], y = j + dirs[idx][1];
                if (0 <= x && x < m && 0 <= y && y < n) {
                    nd = d + (int64_t)((x + 1) * (y + 1) + (((idx & 1) ^ k) * p));
                    if (nd < dist[x][y][k ^ 1]) {
                        dist[x][y][k ^ 1] = nd;
                        pq.emplace(nd, x, y, k ^ 1);
                    }
                }
            }
        }
        return -1;
    }
};
