// LeetCode 2592 - Maximize Greatness of an Array
// https://leetcode.com/problems/maximize-greatness-of-an-array/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximizeGreatness(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int i = 0;
        for (int x : nums) {
            if (x > nums[i]) i++;
        }
        return i;
    }
};
