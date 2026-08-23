// LeetCode 3235 - Check if the Rectangle Corner Is Reachable
// https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/

#include <cstdlib>
#include <functional>
#include <vector>

class Solution {
public:
    bool canReachCorner(int xCorner, int yCorner, std::vector<std::vector<int>>& circles) {
        auto inCircle = [](int x, int y, int cx, int cy, int r) {
            long long dx = x - cx, dy = y - cy;
            return dx * dx + dy * dy <= 1LL * r * r;
        };
        auto crossLeftTop = [&](int cx, int cy, int r) {
            bool a = std::abs(cx) <= r && cy >= 0 && cy <= yCorner;
            bool b = std::abs(cy - yCorner) <= r && cx >= 0 && cx <= xCorner;
            return a || b;
        };
        auto crossRightBottom = [&](int cx, int cy, int r) {
            bool a = std::abs(cx - xCorner) <= r && cy >= 0 && cy <= yCorner;
            bool b = std::abs(cy) <= r && cx >= 0 && cx <= xCorner;
            return a || b;
        };
        int n = (int)circles.size();
        std::vector<char> vis(n, 0);
        std::function<bool(int)> dfs = [&](int i) -> bool {
            int x1 = circles[i][0], y1 = circles[i][1], r1 = circles[i][2];
            if (crossRightBottom(x1, y1, r1)) return true;
            vis[i] = 1;
            for (int j = 0; j < n; j++) {
                if (vis[j]) continue;
                int x2 = circles[j][0], y2 = circles[j][1], r2 = circles[j][2];
                if (1LL * (x1 - x2) * (x1 - x2) + 1LL * (y1 - y2) * (y1 - y2) > 1LL * (r1 + r2) * (r1 + r2)) continue;
                if (1LL * x1 * r2 + 1LL * x2 * r1 < 1LL * (r1 + r2) * xCorner &&
                    1LL * y1 * r2 + 1LL * y2 * r1 < 1LL * (r1 + r2) * yCorner && dfs(j))
                    return true;
            }
            return false;
        };
        for (int i = 0; i < n; i++) {
            int x = circles[i][0], y = circles[i][1], r = circles[i][2];
            if (inCircle(0, 0, x, y, r) || inCircle(xCorner, yCorner, x, y, r)) return false;
            if (!vis[i] && crossLeftTop(x, y, r) && dfs(i)) return false;
        }
        return true;
    }
};
