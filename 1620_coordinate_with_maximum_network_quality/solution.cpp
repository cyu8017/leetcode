// LeetCode 1620 - Coordinate With Maximum Network Quality
// https://leetcode.com/problems/coordinate-with-maximum-network-quality/

#include <cmath>
#include <vector>

class Solution {
public:
    std::vector<int> bestCoordinate(std::vector<std::vector<int>>& towers, int radius) {
        std::vector<int> best{0, 0};
        int quality = -1;
        for (int x = 0; x <= 50; ++x) {
            for (int y = 0; y <= 50; ++y) {
                int q = 0;
                for (const auto& t : towers) {
                    const double d = std::hypot(x - t[0], y - t[1]);
                    if (d <= radius) {
                        q += static_cast<int>(t[2] / (1 + d));
                    }
                }
                if (q > quality) {
                    quality = q;
                    best = {x, y};
                }
            }
        }
        return best;
    }
};
