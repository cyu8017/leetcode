// LeetCode 0034 - Find First and Last Position of Element in Sorted Array
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

#include <vector>

class Solution {
public:
    std::vector<int> searchRange(std::vector<int>& nums, int target) {
        if (nums.empty()) {
            return {-1, -1};
        }

        int start = lowerBound(nums, target);
        if (start == static_cast<int>(nums.size()) || nums[start] != target) {
            return {-1, -1};
        }

        return {start, upperBound(nums, target) - 1};
    }

private:
    int lowerBound(const std::vector<int>& nums, int target) {
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

    int upperBound(const std::vector<int>& nums, int target) {
        int left = 0;
        int right = static_cast<int>(nums.size());

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
};
