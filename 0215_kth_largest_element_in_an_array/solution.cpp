// LeetCode 0215 - Kth Largest Element in an Array
// https://leetcode.com/problems/kth-largest-element-in-an-array/

#include <cstdlib>
#include <ctime>
#include <vector>

class Solution {
    int partition(std::vector<int>& nums, int left, int right) {
        const int pivotIndex = left + std::rand() % (right - left + 1);
        std::swap(nums[pivotIndex], nums[right]);
        int store = left;
        for (int i = left; i < right; ++i) {
            if (nums[i] <= nums[right]) {
                std::swap(nums[store], nums[i]);
                store += 1;
            }
        }
        std::swap(nums[store], nums[right]);
        return store;
    }

public:
    int findKthLargest(std::vector<int>& nums, int k) {
        std::srand(static_cast<unsigned>(std::time(nullptr)));
        const int target = static_cast<int>(nums.size()) - k;
        int left = 0;
        int right = static_cast<int>(nums.size()) - 1;
        while (left <= right) {
            const int pivotIndex = partition(nums, left, right);
            if (pivotIndex == target) {
                return nums[pivotIndex];
            }
            if (pivotIndex < target) {
                left = pivotIndex + 1;
            } else {
                right = pivotIndex - 1;
            }
        }
        return nums[left];
    }
};
