// LeetCode 3870 - Count Commas In Range
// https://leetcode.com/problems/count-commas-in-range/

#include <algorithm>

class Solution {
public:
    int countCommas(int n) {
        return std::max(0, n - 999);
    }
};
