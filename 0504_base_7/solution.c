// LeetCode 0504 - Base 7
// https://leetcode.com/problems/base-7/

#include <stdlib.h>
#include <string.h>

char* convertToBase7(int num) {
    if (num == 0) {
        return strdup("0");
    }

    const int negative = num < 0;
    if (negative) {
        num = -num;
    }

    char digits[32];
    int length = 0;
    while (num > 0) {
        digits[length++] = (char)('0' + num % 7);
        num /= 7;
    }

    char* result = (char*)malloc((size_t)(length + (negative ? 2 : 1)) * sizeof(char));
    int index = 0;
    if (negative) {
        result[index++] = '-';
    }
    for (int digitIndex = length - 1; digitIndex >= 0; digitIndex--) {
        result[index++] = digits[digitIndex];
    }
    result[index] = '\0';
    return result;
}
