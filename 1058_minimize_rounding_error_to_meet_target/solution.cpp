// LeetCode 1058 - Minimize Rounding Error to Meet Target
// https://leetcode.com/problems/minimize-rounding-error-to-meet-target/

#include <algorithm>
#include <cmath>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>

class Solution {
public:
    std::string minimizeError(std::vector<std::string>& prices, int target) {
        int floors = 0;
        std::vector<double> fracs;
        for (const std::string& p : prices) {
            double value = std::stod(p);
            int floor = static_cast<int>(value);
            floors += floor;
            double frac = value - floor;
            if (frac > 1e-9) {
                fracs.push_back(frac);
            }
        }
        int ceilCount = target - floors;
        if (ceilCount < 0 || ceilCount > static_cast<int>(fracs.size())) {
            return "-1";
        }
        std::sort(fracs.begin(), fracs.end(), std::greater<>());
        double error = 0.0;
        for (int i = 0; i < ceilCount; ++i) {
            error += 1.0 - fracs[i];
        }
        for (int i = ceilCount; i < static_cast<int>(fracs.size()); ++i) {
            error += fracs[i];
        }
        std::ostringstream oss;
        oss << std::fixed << std::setprecision(3) << error;
        return oss.str();
    }
};
