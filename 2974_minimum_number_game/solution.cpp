// LeetCode 2974 - Minimum Number Game
// https://leetcode.com/problems/minimum-number-game/

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> numberGame(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        for (int i = 0; i + 1 < (int)nums.size(); i += 2) {
            std::swap(nums[i], nums[i + 1]);
        }
        return nums;
    }
};
