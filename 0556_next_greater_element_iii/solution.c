// LeetCode 0556 - Next Greater Element III
// https://leetcode.com/problems/next-greater-element-iii/

#include <stdio.h>
#include <string.h>

int nextGreaterElement(int n) {
    char digits[16];
    sprintf(digits, "%d", n);
    int len = (int)strlen(digits);
    int i = len - 2;
    while (i >= 0 && digits[i] >= digits[i + 1]) {
        i--;
    }
    if (i < 0) {
        return -1;
    }

    int j = len - 1;
    while (digits[j] <= digits[i]) {
        j--;
    }
    char tmp = digits[i];
    digits[i] = digits[j];
    digits[j] = tmp;

    int left = i + 1;
    int right = len - 1;
    while (left < right) {
        tmp = digits[left];
        digits[left] = digits[right];
        digits[right] = tmp;
        left++;
        right--;
    }

    long long value = 0;
    for (int k = 0; k < len; k++) {
        value = value * 10 + (digits[k] - '0');
    }
    if (value > 2147483647LL) {
        return -1;
    }
    return (int)value;
}
