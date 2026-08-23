// LeetCode 3342 - Find Minimum Time to Reach Last Room II
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

#include <queue>
#include <vector>

class Solution {
public:
    int minTimeToReach(std::vector<std::vector<int>>& moveTime) {
        int m = (int)moveTime.size(), n = (int)moveTime[0].size();
        const int INF = 1 << 30;
        std::vector<std::vector<std::vector<int>>> dist(m, std::vector<std::vector<int>>(n, std::vector<int>(2, INF)));
        using Node = std::tuple<int, int, int, int>; // t, r, c, parity
        std::priority_queue<Node, std::vector<Node>, std::greater<Node>> pq;
        dist[0][0][0] = 0;
        pq.emplace(0, 0, 0, 0);
        int dirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!pq.empty()) {
            auto [t, r, c, parity] = pq.top();
            pq.pop();
            if (t != dist[r][c][parity]) continue;
            if (r == m - 1 && c == n - 1) return t;
            int cost = parity == 1 ? 2 : 1;
            for (auto& d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
                int start = t;
                if (moveTime[nr][nc] > start) start = moveTime[nr][nc];
                int nt = start + cost;
                int np = 1 - parity;
                if (nt < dist[nr][nc][np]) {
                    dist[nr][nc][np] = nt;
                    pq.emplace(nt, nr, nc, np);
                }
            }
        }
        return -1;
    }
};
