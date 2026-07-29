// LeetCode 1956 - Minimum Time For K Virus Variants to Spread
#include <algorithm>
#include <climits>
#include <cstdlib>
#include <vector>

class Solution {
public:
    int minDayskVariants(std::vector<std::vector<int>>& points, int k) {
        int ans = INT_MAX;
        for (int x = 1; x <= 100; x++) {
            for (int y = 1; y <= 100; y++) {
                std::vector<int> dists;
                for (auto& p : points) dists.push_back(std::abs(p[0] - x) + std::abs(p[1] - y));
                std::sort(dists.begin(), dists.end());
                ans = std::min(ans, dists[k - 1]);
            }
        }
        return ans;
    }
};
