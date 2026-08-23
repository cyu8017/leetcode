// LeetCode 3667 - Sort Array By Absolute Value
// https://leetcode.com/problems/sort-array-by-absolute-value/

#include <algorithm>
#include <cmath>
#include <vector>

class Solution {
public:
    std::vector<int> sortByAbsoluteValue(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end(), [](int a, int b) { return std::abs(a) < std::abs(b); });
        return nums;
    }
};
