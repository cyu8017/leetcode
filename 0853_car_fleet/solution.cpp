// LeetCode 0853 - Car Fleet
// https://leetcode.com/problems/car-fleet/

#include <algorithm>
#include <utility>
#include <vector>

class Solution {
public:
    int carFleet(int target, std::vector<int>& position, std::vector<int>& speed) {
        int n = static_cast<int>(position.size());
        std::vector<std::pair<int, int>> cars;
        for (int i = 0; i < n; ++i) {
            cars.emplace_back(position[i], speed[i]);
        }
        std::sort(cars.begin(), cars.end(), std::greater<>());
        int fleets = 0;
        double maxTime = 0.0;
        for (auto [pos, spd] : cars) {
            double time = static_cast<double>(target - pos) / spd;
            if (time > maxTime) {
                ++fleets;
                maxTime = time;
            }
        }
        return fleets;
    }
};
