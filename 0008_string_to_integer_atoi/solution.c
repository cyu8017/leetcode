// LeetCode 0008 - String to Integer (atoi)
// https://leetcode.com/problems/string-to-integer-atoi/

#include <ctype.h>
#include <limits.h>

int myAtoi(char* s) {
    int i = 0;
    while (s[i] == ' ') {
        i++;
    }
    if (s[i] == '\0') {
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
    while (s[i] >= '0' && s[i] <= '9') {
        int digit = s[i] - '0';
        if (result > (INT_MAX - digit) / 10) {
            return sign == -1 ? INT_MIN : INT_MAX;
        }
        result = result * 10 + digit;
        i++;
    }

    return sign * result;
}
