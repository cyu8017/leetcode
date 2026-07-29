// LeetCode 1291 - Sequential Digits
// https://leetcode.com/problems/sequential-digits/

#include <stdlib.h>

int* sequentialDigits(int low, int high, int* returnSize) {
    const char* digits = "123456789";
    int cap = 64, count = 0;
    int* ans = (int*)malloc((size_t)cap * sizeof(int));
    for (int length = 2; length <= 9; length++) {
        for (int start = 0; start + length <= 9; start++) {
            int value = 0;
            for (int i = 0; i < length; i++) value = value * 10 + (digits[start + i] - '0');
            if (value >= low && value <= high) {
                if (count >= cap) {
                    cap *= 2;
                    ans = (int*)realloc(ans, (size_t)cap * sizeof(int));
                }
                ans[count++] = value;
            }
        }
    }
    *returnSize = count;
    ans = (int*)realloc(ans, (size_t)count * sizeof(int));
    return ans;
}
