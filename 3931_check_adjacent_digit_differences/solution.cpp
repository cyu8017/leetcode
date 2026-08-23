// LeetCode 3931 - Check Adjacent Digit Differences
// https://leetcode.com/problems/check-adjacent-digit-differences/

#include <cmath>
#include <string>

class Solution {
public:
    bool isAdjacentDiffAtMostTwo(std::string s) {
        for (int i = 1; i < (int)s.size(); i++) {
            if (std::abs((int)s[i - 1] - (int)s[i]) > 2) return false;
        }
        return true;
    }
};
