// LeetCode 3382 - Maximum Area Rectangle With Point Constraints II
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/

#include <cstdint>
#include <set>
#include <utility>
#include <vector>

class Solution {
public:
    long long maxRectangleArea(std::vector<int>& xCoord, std::vector<int>& yCoord) {
        int n = (int)xCoord.size();
        std::vector<std::vector<int>> points(n);
        for (int i = 0; i < n; i++) points[i] = {xCoord[i], yCoord[i]};
        std::set<std::pair<int, int>> set;
        for (auto& p : points) set.insert({p[0], p[1]});
        long long ans = -1;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int x1 = points[i][0], y1 = points[i][1];
                int x2 = points[j][0], y2 = points[j][1];
                if (x1 == x2 || y1 == y2) continue;
                if (!set.count({x1, y2}) || !set.count({x2, y1})) continue;
                int minX = std::min(x1, x2), maxX = std::max(x1, x2);
                int minY = std::min(y1, y2), maxY = std::max(y1, y2);
                bool ok = true;
                for (auto& p : points) {
                    int x = p[0], y = p[1];
                    if (x > minX && x < maxX && y > minY && y < maxY) { ok = false; break; }
                    bool onBorder = ((x == minX || x == maxX) && y >= minY && y <= maxY) ||
                                    ((y == minY || y == maxY) && x >= minX && x <= maxX);
                    if (onBorder) {
                        bool isCorner = (x == minX || x == maxX) && (y == minY || y == maxY);
                        if (!isCorner) { ok = false; break; }
                    }
                }
                if (ok) {
                    long long area = (long long)(maxX - minX) * (maxY - minY);
                    if (area > ans) ans = area;
                }
            }
        }
        return ans;
    }
};
