// LeetCode 2553 - Separate the Digits in an Array
// https://leetcode.com/problems/separate-the-digits-in-an-array/

#include <vector>

class Solution {
public:
    std::vector<int> separateDigits(std::vector<int>& nums) {
        std::vector<int> ans;
        for (int x : nums) {
            std::vector<int> digits;
            while (x > 0) {
                digits.push_back(x % 10);
                x /= 10;
            }
            for (int i = (int)digits.size() - 1; i >= 0; --i) ans.push_back(digits[i]);
        }
        return ans;
    }
};
