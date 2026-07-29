// LeetCode 0789 - Escape The Ghosts
// https://leetcode.com/problems/escape-the-ghosts/

#include <cstdlib>
#include <vector>

class Solution {
public:
    bool escapeGhosts(std::vector<std::vector<int>>& ghosts, std::vector<int>& target) {
        int targetDist = std::abs(target[0]) + std::abs(target[1]);
        for (const auto& ghost : ghosts) {
            if (std::abs(ghost[0] - target[0]) + std::abs(ghost[1] - target[1]) <= targetDist) {
                return false;
            }
        }
        return true;
    }
};
