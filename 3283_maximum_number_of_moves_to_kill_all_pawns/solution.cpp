// LeetCode 3283 - Maximum Number of Moves to Kill All Pawns
// https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/

#include <array>
#include <functional>
#include <map>
#include <queue>
#include <utility>
#include <vector>

class Solution {
    std::vector<int> knightDist(int x, int y, const std::vector<std::array<int, 2>>& pts) {
        static const int dirs[8][2] = {{1, 2}, {1, -2}, {-1, 2}, {-1, -2}, {2, 1}, {2, -1}, {-2, 1}, {-2, -1}};
        int np = (int)pts.size();
        std::vector<int> ans(np, -1);
        bool vis[50][50] = {};
        std::queue<std::array<int, 3>> q;
        q.push({x, y, 0});
        vis[x][y] = true;
        std::map<std::pair<int, int>, std::vector<int>> need;
        for (int i = 0; i < np; i++) need[{pts[i][0], pts[i][1]}].push_back(i);
        int found = 0;
        while (!q.empty() && found < np) {
            auto cur = q.front();
            q.pop();
            auto key = std::make_pair(cur[0], cur[1]);
            auto it = need.find(key);
            if (it != need.end()) {
                for (int i : it->second) {
                    if (ans[i] == -1) {
                        ans[i] = cur[2];
                        found++;
                    }
                }
            }
            for (auto& d : dirs) {
                int nx = cur[0] + d[0], ny = cur[1] + d[1];
                if (nx < 0 || ny < 0 || nx >= 50 || ny >= 50 || vis[nx][ny]) continue;
                vis[nx][ny] = true;
                q.push({nx, ny, cur[2] + 1});
            }
        }
        return ans;
    }

public:
    int maxMoves(int kx, int ky, std::vector<std::vector<int>>& positions) {
        int n = (int)positions.size();
        std::vector<std::array<int, 2>> pts(n + 1);
        pts[0] = {kx, ky};
        for (int i = 0; i < n; i++) pts[i + 1] = {positions[i][0], positions[i][1]};
        std::vector<std::vector<int>> dist(n + 1);
        for (int i = 0; i <= n; i++) dist[i] = knightDist(pts[i][0], pts[i][1], pts);
        int N = 1 << n;
        std::vector<std::vector<int>> memo(N, std::vector<int>(n + 1, -1));
        std::function<int(int, int, int)> dfs = [&](int mask, int cur, int turn) -> int {
            if (mask == N - 1) return 0;
            if (memo[mask][cur] != -1) return memo[mask][cur];
            int best = turn == 0 ? -(1 << 30) : (1 << 30);
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) continue;
                int d = dist[cur][i + 1];
                int v = d + dfs(mask | (1 << i), i + 1, 1 - turn);
                if (turn == 0) {
                    if (v > best) best = v;
                } else if (v < best) best = v;
            }
            return memo[mask][cur] = best;
        };
        return dfs(0, 0, 0);
    }
};
