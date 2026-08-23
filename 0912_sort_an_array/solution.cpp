// LeetCode 0912 - Sort an Array
// https://leetcode.com/problems/sort-an-array/

#include <vector>

class Solution {
public:
    std::vector<int> sortArray(std::vector<int>& nums) {
        if (nums.size() <= 1) return nums;
        int mid = (int)nums.size() / 2;
        std::vector<int> left(nums.begin(), nums.begin() + mid);
        std::vector<int> right(nums.begin() + mid, nums.end());
        left = sortArray(left);
        right = sortArray(right);
        std::vector<int> merged;
        merged.reserve(nums.size());
        int i = 0, j = 0;
        while (i < (int)left.size() && j < (int)right.size()) {
            if (left[i] <= right[j]) merged.push_back(left[i++]);
            else merged.push_back(right[j++]);
        }
        while (i < (int)left.size()) merged.push_back(left[i++]);
        while (j < (int)right.size()) merged.push_back(right[j++]);
        return merged;
    }
};
