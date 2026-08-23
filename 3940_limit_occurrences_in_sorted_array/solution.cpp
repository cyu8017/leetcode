// LeetCode 3940 - Limit Occurrences In Sorted Array
// https://leetcode.com/problems/limit-occurrences-in-sorted-array/

#include <vector>

class Solution {
public:
    std::vector<int> limitOccurrences(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        int cnt = 1, l = 1;
        for (int r = 1; r < n; r++) {
            if (nums[r] != nums[r - 1]) cnt = 1;
            else cnt++;
            if (cnt <= k) {
                nums[l] = nums[r];
                l++;
            }
        }
        nums.resize(l);
        return nums;
    }
};
