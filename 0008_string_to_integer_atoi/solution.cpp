// LeetCode 0008 - String to Integer (atoi)
// https://leetcode.com/problems/string-to-integer-atoi/

#include <cctype>
#include <climits>
#include <string>

class Solution {
public:
    int myAtoi(std::string s) {
        int i = 0;
        int n = static_cast<int>(s.size());
        while (i < n && s[i] == ' ') {
            i++;
        }
        if (i >= n) {
            return 0;
        }

        int sign = 1;
        if (s[i] == '-') {
            sign = -1;
            i++;
        } else if (s[i] == '+') {
            i++;
        }

        int result = 0;
        while (i < n && std::isdigit(static_cast<unsigned char>(s[i]))) {
            int digit = s[i] - '0';
            if (result > (INT_MAX - digit) / 10) {
                return sign == -1 ? INT_MIN : INT_MAX;
            }
            result = result * 10 + digit;
            i++;
        }

        return sign * result;
    }
};
