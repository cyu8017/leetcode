// LeetCode 2243 - Calculate Digit Sum of a String
// https://leetcode.com/problems/calculate-digit-sum-of-a-string/

#include <string>

class Solution {
public:
    std::string digitSum(std::string s, int k) {
        while ((int)s.size() > k) {
            std::string next;
            for (size_t i = 0; i < s.size(); i += k) {
                int sum = 0;
                size_t end = std::min(i + (size_t)k, s.size());
                for (size_t j = i; j < end; ++j) sum += s[j] - '0';
                next += std::to_string(sum);
            }
            s = next;
        }
        return s;
    }
};
