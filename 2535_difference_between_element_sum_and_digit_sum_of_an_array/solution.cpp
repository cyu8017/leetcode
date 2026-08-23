// LeetCode 2535 - Difference Between Element Sum and Digit Sum of an Array
// https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

#include <cstdlib>
#include <vector>

class Solution {
public:
    int differenceOfSum(std::vector<int>& nums) {
        int elem = 0, digit = 0;
        for (int x : nums) {
            elem += x;
            while (x > 0) {
                digit += x % 10;
                x /= 10;
            }
        }
        return std::abs(elem - digit);
    }
};
