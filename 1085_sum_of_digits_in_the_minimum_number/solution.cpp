// LeetCode 1085 - Sum of Digits in the Minimum Number
// https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/

#include <algorithm>
#include <vector>

class Solution {
public:
    int sumOfDigits(std::vector<int>& nums) {
        int n = *std::min_element(nums.begin(), nums.end());
        int digitSum = 0;
        while (n) {
            digitSum += n % 10;
            n /= 10;
        }
        return digitSum % 2 == 0 ? 1 : 0;
    }
};
