// LeetCode 2578 - Split With Minimum Sum
// https://leetcode.com/problems/split-with-minimum-sum/

#include <algorithm>
#include <vector>

class Solution {
public:
    int splitNum(int num) {
        std::vector<int> digits;
        while (num > 0) {
            digits.push_back(num % 10);
            num /= 10;
        }
        std::sort(digits.begin(), digits.end());
        int a = 0, b = 0;
        for (int i = 0; i < (int)digits.size(); ++i) {
            if (i % 2 == 0) a = a * 10 + digits[i];
            else b = b * 10 + digits[i];
        }
        return a + b;
    }
};
