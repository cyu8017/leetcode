// LeetCode 1870 - Minimum Speed to Arrive on Time
// https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

#include <vector>

class Solution {
public:
    int minSpeedOnTime(std::vector<int>& dist, double hour) {
        int n = static_cast<int>(dist.size());
        if (n - 1 >= hour) {
            return -1;
        }

        auto canArrive = [&](int speed) {
            double time = 0.0;
            for (int i = 0; i < n - 1; i++) {
                time += (dist[i] + speed - 1) / speed;
            }
            time += static_cast<double>(dist.back()) / speed;
            return time <= hour;
        };

        if (!canArrive(10000000)) {
            return -1;
        }

        int lo = 1;
        int hi = 10000000;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (canArrive(mid)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
};
