// LeetCode 0625 - Minimum Factorization
// https://leetcode.com/problems/minimum-factorization/

#include <vector>

class Solution {
public:
    int smallestFactorization(int num) {
        if (num < 10) {
            return num;
        }
        std::vector<int> digits;
        for (int digit = 9; digit >= 2; --digit) {
            while (num % digit == 0) {
                digits.push_back(digit);
                num /= digit;
            }
        }
        if (num != 1) {
            return 0;
        }
        long long result = 0;
        for (int i = static_cast<int>(digits.size()) - 1; i >= 0; --i) {
            result = result * 10 + digits[i];
            if (result > 2147483647LL) {
                return 0;
            }
        }
        return static_cast<int>(result);
    }
};
