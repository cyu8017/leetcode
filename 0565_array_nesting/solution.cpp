// LeetCode 0565 - Array Nesting
// https://leetcode.com/problems/array-nesting/

#include <algorithm>
#include <vector>

class Solution {
public:
    int arrayNesting(std::vector<int>& nums) {
        int best = 0;
        for (std::size_t i = 0; i < nums.size(); ++i) {
            if (nums[i] < 0) {
                continue;
            }
            int length = 0;
            int j = static_cast<int>(i);
            while (nums[j] >= 0) {
                int nxt = nums[j];
                nums[j] = -1;
                j = nxt;
                ++length;
            }
            best = std::max(best, length);
        }
        return best;
    }
};
