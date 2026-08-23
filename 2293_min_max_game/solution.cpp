// LeetCode 2293 - Min Max Game
// https://leetcode.com/problems/min-max-game/

#include <vector>
#include <algorithm>

class Solution {
public:
    int minMaxGame(std::vector<int>& nums) {
        while (nums.size() > 1) {
            std::vector<int> next(nums.size() / 2);
            for (size_t i = 0; i < next.size(); ++i) {
                if (i % 2 == 0) next[i] = std::min(nums[2 * i], nums[2 * i + 1]);
                else next[i] = std::max(nums[2 * i], nums[2 * i + 1]);
            }
            nums = std::move(next);
        }
        return nums[0];
    }
};
