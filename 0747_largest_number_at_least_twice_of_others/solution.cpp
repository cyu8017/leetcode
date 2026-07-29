// LeetCode 0747 - Largest Number At Least Twice of Others
// https://leetcode.com/problems/largest-number-at-least-twice-of-others/

#include <vector>

class Solution {
public:
    int dominantIndex(std::vector<int>& nums) {
        int first = -1;
        int second = -1;
        int index = -1;
        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            if (nums[i] > first) {
                second = first;
                first = nums[i];
                index = i;
            } else if (nums[i] > second) {
                second = nums[i];
            }
        }
        return first >= 2 * second ? index : -1;
    }
};
