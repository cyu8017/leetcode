// LeetCode 2529 - Maximum Count of Positive Integer and Negative Integer
// https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximumCount(std::vector<int>& nums) {
        int pos = 0, neg = 0;
        for (int x : nums) {
            if (x > 0) pos++;
            else if (x < 0) neg++;
        }
        return std::max(pos, neg);
    }
};
