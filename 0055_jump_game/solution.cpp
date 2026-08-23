// LeetCode 0055 - Jump Game
// https://leetcode.com/problems/jump-game/

#include <algorithm>
#include <vector>

class Solution {
public:
    bool canJump(std::vector<int>& nums) {
        int farthest = 0;

        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            if (i > farthest) {
                return false;
            }
            farthest = std::max(farthest, i + nums[i]);
        }

        return true;
    }
};
