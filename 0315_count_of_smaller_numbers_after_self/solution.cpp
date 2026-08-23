// LeetCode 0315 - Count of Smaller Numbers After Self
// https://leetcode.com/problems/count-of-smaller-numbers-after-self/

#include <vector>

class Solution {
public:
    std::vector<int> countSmaller(std::vector<int>& nums) {
        std::vector<int> sortedNums;
        std::vector<int> result(nums.size(), 0);

        for (int index = static_cast<int>(nums.size()) - 1; index >= 0; index--) {
            int num = nums[index];
            int left = 0;
            int right = static_cast<int>(sortedNums.size());
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (sortedNums[mid] < num) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            result[index] = left;
            sortedNums.insert(sortedNums.begin() + left, num);
        }

        return result;
    }
};
