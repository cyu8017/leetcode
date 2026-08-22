// LeetCode 2864 - Maximum Odd Binary Number
// https://leetcode.com/problems/maximum-odd-binary-number/

#include <stdlib.h>
#include <string.h>

char* maximumOddBinaryNumber(char* s) {
    int n = (int)strlen(s), ones = 0;
    for (int i = 0; i < n; i++) if (s[i] == '1') ones++;
    int zeros = n - ones;
    char* b = (char*)malloc(n + 1);
    int p = 0;
    for (int i = 0; i < ones - 1; i++) b[p++] = '1';
    for (int i = 0; i < zeros; i++) b[p++] = '0';
    b[p++] = '1';
    b[p] = '\0';
    return b;
}
