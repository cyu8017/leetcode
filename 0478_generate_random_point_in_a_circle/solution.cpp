// LeetCode 0478 - Generate Random Point in a Circle
// https://leetcode.com/problems/generate-random-point-in-a-circle/

#include <cmath>
#include <cstdlib>
#include <functional>
#include <vector>

namespace {
std::function<double(double, double)> uniform = [](double low, double high) {
    return low + (high - low) * (static_cast<double>(std::rand()) / RAND_MAX);
};
}  // namespace

void set_uniform(std::function<double(double, double)> uniform_fn) {
    uniform = std::move(uniform_fn);
}

class Solution {
    double radius_;
    double xCenter_;
    double yCenter_;

public:
    Solution(double radius, double xCenter, double yCenter)
        : radius_(radius), xCenter_(xCenter), yCenter_(yCenter) {}

    std::vector<double> randPoint() {
        while (true) {
            const double x = uniform(-radius_, radius_);
            const double y = uniform(-radius_, radius_);
            if (x * x + y * y <= radius_ * radius_) {
                const double roundedX = std::round((xCenter_ + x) * 100000.0) / 100000.0;
                const double roundedY = std::round((yCenter_ + y) * 100000.0) / 100000.0;
                return {roundedX, roundedY};
            }
        }
    }
};
