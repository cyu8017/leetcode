// LeetCode 3341 - Find Minimum Time to Reach Last Room I
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

#include <array>
#include <queue>
#include <vector>

class Solution {
public:
    int minTimeToReach(std::vector<std::vector<int>>& moveTime) {
        int m = (int)moveTime.size(), n = (int)moveTime[0].size();
        std::vector<std::vector<int>> dist(m, std::vector<int>(n, 1 << 30));
        using Node = std::array<int, 3>; // t, r, c
        std::priority_queue<Node, std::vector<Node>, std::greater<Node>> h;
        h.push({0, 0, 0});
        dist[0][0] = 0;
        const int dirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!h.empty()) {
            auto cur = h.top(); h.pop();
            int t = cur[0], r = cur[1], c = cur[2];
            if (t != dist[r][c]) continue;
            if (r == m - 1 && c == n - 1) return t;
            for (auto& d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
                int start = t;
                if (moveTime[nr][nc] > start) start = moveTime[nr][nc];
                int nt = start + 1;
                if (nt < dist[nr][nc]) {
                    dist[nr][nc] = nt;
                    h.push({nt, nr, nc});
                }
            }
        }
        return -1;
    }
};
