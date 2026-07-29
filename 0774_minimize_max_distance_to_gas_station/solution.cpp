// LeetCode 0774 - Minimize Max Distance to Gas Station
// https://leetcode.com/problems/minimize-max-distance-to-gas-station/

#include <vector>

class Solution {
public:
    double minmaxGasDist(std::vector<int>& stations, int k) {
        auto can = [&](double dist) {
            int needed = 0;
            for (size_t i = 1; i < stations.size(); ++i) {
                needed += static_cast<int>((stations[i] - stations[i - 1]) / dist);
            }
            return needed <= k;
        };
        double lo = 0.0;
        double hi = static_cast<double>(stations.back() - stations.front());
        while (hi - lo > 1e-6) {
            double mid = (lo + hi) / 2.0;
            if (can(mid)) {
                hi = mid;
            } else {
                lo = mid;
            }
        }
        return hi;
    }
};
