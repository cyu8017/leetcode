// LeetCode 1558 - Minimum Numbers of Function Calls to Make Target Array
// https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        int bit_sum = 0;
        int max_length = 0;
        for (int x : nums) {
            bit_sum += __builtin_popcount(static_cast<unsigned>(x));
            if (x > 0) {
                max_length = std::max(max_length, 31 - __builtin_clz(static_cast<unsigned>(x)));
            }
        }
        return bit_sum + max_length;
    }
};
