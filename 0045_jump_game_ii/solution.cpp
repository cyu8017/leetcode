// LeetCode 0045 - Jump Game II
// https://leetcode.com/problems/jump-game-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int jump(std::vector<int>& nums) {
        int jumps = 0;
        int currentEnd = 0;
        int farthest = 0;

        for (int i = 0; i < static_cast<int>(nums.size()) - 1; i++) {
            farthest = std::max(farthest, i + nums[i]);
            if (i == currentEnd) {
                jumps++;
                currentEnd = farthest;
            }
        }

        return jumps;
    }
};
