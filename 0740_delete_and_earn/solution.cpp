// LeetCode 0740 - Delete and Earn
// https://leetcode.com/problems/delete-and-earn/

#include <algorithm>
#include <vector>

class Solution {
public:
    int deleteAndEarn(std::vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        int maxNum = *std::max_element(nums.begin(), nums.end());
        std::vector<int> points(maxNum + 1, 0);
        for (int num : nums) {
            points[num] += num;
        }
        int take = 0;
        int skip = 0;
        for (int value : points) {
            int newTake = skip + value;
            int newSkip = std::max(skip, take);
            take = newTake;
            skip = newSkip;
        }
        return std::max(take, skip);
    }
};
