// LeetCode 2283 - Check if Number Has Equal Digit Count and Digit Value
// https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

#include <string>
#include <vector>

class Solution {
public:
    bool digitCount(std::string num) {
        std::vector<int> cnt(10);
        for (char c : num) cnt[c - '0']++;
        for (size_t i = 0; i < num.size(); ++i)
            if (cnt[i] != num[i] - '0') return false;
        return true;
    }
};
