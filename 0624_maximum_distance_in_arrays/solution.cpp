// LeetCode 0624 - Maximum Distance in Arrays
// https://leetcode.com/problems/maximum-distance-in-arrays/

#include <algorithm>
#include <cstdlib>
#include <vector>

class Solution {
public:
    int maxDistance(std::vector<std::vector<int>>& arrays) {
        int minVal = arrays[0].front();
        int maxVal = arrays[0].back();
        int best = 0;
        for (std::size_t i = 1; i < arrays.size(); ++i) {
            best = std::max(
                {best, std::abs(arrays[i].back() - minVal), std::abs(maxVal - arrays[i].front())});
            minVal = std::min(minVal, arrays[i].front());
            maxVal = std::max(maxVal, arrays[i].back());
        }
        return best;
    }
};
