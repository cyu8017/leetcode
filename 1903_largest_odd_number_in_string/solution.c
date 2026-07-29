// LeetCode 1903 - Largest Odd Number in String
// https://leetcode.com/problems/largest-odd-number-in-string/

#include <stdlib.h>
#include <string.h>

char* largestOddNumber(char* num) {
    int n = (int)strlen(num);
    for (int i = n - 1; i >= 0; i--) {
        if ((num[i] - '0') % 2 == 1) {
            char* res = (char*)malloc((size_t)i + 2);
            memcpy(res, num, (size_t)i + 1);
            res[i + 1] = '\0';
            return res;
        }
    }
    char* empty = (char*)malloc(1);
    empty[0] = '\0';
    return empty;
}
