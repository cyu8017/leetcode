// LeetCode 0031 - Next Permutation
// https://leetcode.com/problems/next-permutation/

#include <vector>

class Solution {
public:
    void nextPermutation(std::vector<int>& nums) {
        int i = static_cast<int>(nums.size()) - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }

        if (i >= 0) {
            int j = static_cast<int>(nums.size()) - 1;
            while (nums[j] <= nums[i]) {
                j--;
            }
            std::swap(nums[i], nums[j]);
        }

        int left = i + 1;
        int right = static_cast<int>(nums.size()) - 1;
        while (left < right) {
            std::swap(nums[left], nums[right]);
            left++;
            right--;
        }
    }
};
