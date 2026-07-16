// LeetCode 0493 - Reverse Pairs
// https://leetcode.com/problems/reverse-pairs/

#include <algorithm>
#include <vector>

class Solution {
    long long mergeSort(std::vector<int>& nums, int start, int end) {
        if (start >= end) {
            return 0;
        }
        const int mid = start + (end - start) / 2;
        long long count = mergeSort(nums, start, mid) + mergeSort(nums, mid + 1, end);
        int j = mid + 1;
        for (int i = start; i <= mid; ++i) {
            while (j <= end && static_cast<long long>(nums[i]) > 2LL * nums[j]) {
                ++j;
            }
            count += j - (mid + 1);
        }
        std::inplace_merge(nums.begin() + start, nums.begin() + mid + 1, nums.begin() + end + 1);
        return count;
    }

public:
    int reversePairs(std::vector<int>& nums) {
        return static_cast<int>(mergeSort(nums, 0, static_cast<int>(nums.size()) - 1));
    }
};
