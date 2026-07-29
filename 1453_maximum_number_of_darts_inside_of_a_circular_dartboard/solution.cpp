#include <cmath>
#include <vector>

class Solution {
public:
    int numPoints(std::vector<std::vector<int>>& darts, int r) {
        int ans = darts.empty() ? 0 : 1;
        int n = (int)darts.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                double x1 = darts[i][0], y1 = darts[i][1];
                double x2 = darts[j][0], y2 = darts[j][1];
                double dx = x2 - x1, dy = y2 - y1;
                double d2 = dx * dx + dy * dy;
                if (d2 > 4.0 * r * r || d2 == 0) continue;
                double d = std::sqrt(d2);
                double h = std::sqrt(r * r - d2 / 4.0);
                double mx = (x1 + x2) / 2, my = (y1 + y2) / 2;
                for (int sign : {-1, 1}) {
                    double cx = mx + sign * (-dy) * h / d;
                    double cy = my + sign * dx * h / d;
                    int cnt = 0;
                    for (auto& p : darts) {
                        double ex = p[0] - cx, ey = p[1] - cy;
                        if (ex * ex + ey * ey <= r * r + 1e-7) ++cnt;
                    }
                    ans = std::max(ans, cnt);
                }
            }
        }
        return ans;
    }
};
