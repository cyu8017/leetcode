// LeetCode 0963 - Minimum Area Rectangle II
// https://leetcode.com/problems/minimum-area-rectangle-ii/

#include <cmath>
#include <map>
#include <utility>
#include <vector>

class Solution {
public:
    double minAreaFreeRect(std::vector<std::vector<int>>& points) {
        int n = (int)points.size();
        std::map<std::pair<std::pair<long long, long long>, long long>,
                 std::vector<std::pair<int, int>>> groups;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                long long cx = points[i][0] + points[j][0];
                long long cy = points[i][1] + points[j][1];
                long long dx = points[i][0] - points[j][0];
                long long dy = points[i][1] - points[j][1];
                long long dist = dx * dx + dy * dy;
                groups[{{cx, cy}, dist}].push_back({i, j});
            }
        }
        double ans = 1e300;
        for (auto& [_, pairs] : groups) {
            for (int a = 0; a < (int)pairs.size(); a++) {
                for (int b = a + 1; b < (int)pairs.size(); b++) {
                    int p1 = pairs[a].first, p2 = pairs[b].first, q2 = pairs[b].second;
                    double d1 = std::hypot(points[p1][0] - points[p2][0], points[p1][1] - points[p2][1]);
                    double d2 = std::hypot(points[p1][0] - points[q2][0], points[p1][1] - points[q2][1]);
                    double area = d1 * d2;
                    if (area > 0) ans = std::min(ans, area);
                }
            }
        }
        return ans >= 1e299 ? 0.0 : ans;
    }
};
