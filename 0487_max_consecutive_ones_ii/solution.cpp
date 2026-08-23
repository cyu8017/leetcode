// LeetCode 0487 - Max Consecutive Ones II
// https://leetcode.com/problems/max-consecutive-ones-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int findMaxConsecutiveOnes(std::vector<int>& nums) {
        int left = 0;
        int best = 0;
        int zeros = 0;
        for (int right = 0; right < static_cast<int>(nums.size()); ++right) {
            if (nums[right] == 0) {
                ++zeros;
            }
            while (zeros > 1) {
                if (nums[left] == 0) {
                    --zeros;
                }
                ++left;
            }
            best = std::max(best, right - left + 1);
        }
        return best;
    }
};
