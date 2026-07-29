// LeetCode 1515 - Best Position for a Service Centre
// https://leetcode.com/problems/best-position-for-a-service-centre/

#include <cmath>
#include <utility>
#include <vector>

class Solution {
public:
    double getMinDistSum(std::vector<std::vector<int>>& positions) {
        double x = 0.0;
        double y = 0.0;
        for (const auto& p : positions) {
            x += p[0];
            y += p[1];
        }
        x /= positions.size();
        y /= positions.size();

        auto distance = [&](double a, double b) {
            double total = 0.0;
            for (const auto& p : positions) {
                total += std::hypot(a - p[0], b - p[1]);
            }
            return total;
        };

        for (int iter = 0; iter < 10000; ++iter) {
            double numerator_x = 0.0;
            double numerator_y = 0.0;
            double denominator = 0.0;
            bool coincident = false;
            double cx = 0.0;
            double cy = 0.0;
            for (const auto& p : positions) {
                const double d = std::hypot(x - p[0], y - p[1]);
                if (d < 1e-12) {
                    coincident = true;
                    cx = p[0];
                    cy = p[1];
                    break;
                }
                numerator_x += p[0] / d;
                numerator_y += p[1] / d;
                denominator += 1.0 / d;
            }
            const double nx = coincident ? cx : numerator_x / denominator;
            const double ny = coincident ? cy : numerator_y / denominator;
            if (std::hypot(nx - x, ny - y) < 1e-8) {
                x = nx;
                y = ny;
                break;
            }
            x = nx;
            y = ny;
        }
        return distance(x, y);
    }
};
