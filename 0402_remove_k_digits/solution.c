// LeetCode 0402 - Remove K Digits
// https://leetcode.com/problems/remove-k-digits/

#include <stdlib.h>
#include <string.h>

char* removeKdigits(char* num, int k) {
    int length = (int)strlen(num);
    char* stack = (char*)malloc((size_t)length + 1);
    int stackSize = 0;

    for (int index = 0; index < length; index++) {
        char digit = num[index];
        while (k > 0 && stackSize > 0 && stack[stackSize - 1] > digit) {
            stackSize -= 1;
            k -= 1;
        }
        stack[stackSize++] = digit;
    }

    if (k > 0) {
        stackSize -= k;
    }

    int start = 0;
    while (start < stackSize - 1 && stack[start] == '0') {
        start += 1;
    }

    char* result = (char*)malloc((size_t)(stackSize - start + 1));
    memcpy(result, stack + start, (size_t)(stackSize - start));
    result[stackSize - start] = '\0';
    free(stack);

    if (result[0] == '\0') {
        free(result);
        return strdup("0");
    }

    return result;
}
