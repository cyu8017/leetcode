// LeetCode 0324 - Wiggle Sort II
// https://leetcode.com/problems/wiggle-sort-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    void wiggleSort(std::vector<int>& nums) {
        std::vector<int> sortedNums = nums;
        std::sort(sortedNums.begin(), sortedNums.end());
        int left = (static_cast<int>(nums.size()) - 1) / 2;
        int right = static_cast<int>(nums.size()) - 1;
        for (int index = 0; index < static_cast<int>(nums.size()); index++) {
            if (index % 2 == 0) {
                nums[index] = sortedNums[left--];
            } else {
                nums[index] = sortedNums[right--];
            }
        }
    }
};
