// LeetCode 3723 - Maximize Sum of Squares of Digits
// https://leetcode.com/problems/maximize-sum-of-squares-of-digits/

#include <string>

class Solution {
public:
    std::string maxSumOfSquares(int num, int sum) {
        if (num * 9 < sum) return "";
        int k = sum / 9, s = sum % 9;
        std::string ans(k, '9');
        if (s > 0) ans.push_back(char('0' + s));
        if ((int)ans.size() < num) ans.append(num - (int)ans.size(), '0');
        return ans;
    }
};
