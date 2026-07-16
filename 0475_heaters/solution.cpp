// LeetCode 0475 - Heaters
// https://leetcode.com/problems/heaters/

#include <algorithm>
#include <cmath>
#include <vector>

class Solution {
public:
    int findRadius(std::vector<int>& houses, std::vector<int>& heaters) {
        std::sort(heaters.begin(), heaters.end());
        int radius = 0;
        for (int house : houses) {
            const auto position = std::lower_bound(heaters.begin(), heaters.end(), house);
            int best = static_cast<int>(1e9);
            if (position != heaters.end()) {
                best = std::min(best, std::abs(*position - house));
            }
            if (position != heaters.begin()) {
                best = std::min(best, std::abs(*(position - 1) - house));
            }
            radius = std::max(radius, best);
        }
        return radius;
    }
};
