// LeetCode 1702 - Maximum Binary String After Change
// https://leetcode.com/problems/maximum-binary-string-after-change/

#include <stdlib.h>
#include <string.h>

char* maximumBinaryString(char* binary) {
    int n = (int)strlen(binary);
    int zeros = 0;
    int first = -1;
    for (int i = 0; i < n; i++) {
        if (binary[i] == '0') {
            zeros++;
            if (first < 0) {
                first = i;
            }
        }
    }
    char* result = (char*)malloc(n + 1);
    if (zeros <= 1) {
        strcpy(result, binary);
        return result;
    }
    memset(result, '1', n);
    result[first + zeros - 1] = '0';
    result[n] = '\0';
    return result;
}
