// LeetCode 0035 - Search Insert Position
// https://leetcode.com/problems/search-insert-position/

#include <vector>

class Solution {
public:
    int searchInsert(std::vector<int>& nums, int target) {
        int left = 0;
        int right = static_cast<int>(nums.size());

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
};
