// LeetCode 0447 - Number of Boomerangs
// https://leetcode.com/problems/number-of-boomerangs/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int numberOfBoomerangs(std::vector<std::vector<int>>& points) {
        int total = 0;
        for (const auto& anchor : points) {
            std::unordered_map<long long, int> distances;
            for (const auto& other : points) {
                long long dx = static_cast<long long>(anchor[0]) - other[0];
                long long dy = static_cast<long long>(anchor[1]) - other[1];
                ++distances[dx * dx + dy * dy];
            }
            for (const auto& entry : distances) {
                total += entry.second * (entry.second - 1);
            }
        }
        return total;
    }
};
