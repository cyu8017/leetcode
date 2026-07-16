// LeetCode 0541 - Reverse String II
// https://leetcode.com/problems/reverse-string-ii/

#include <string.h>

static void reverse_range(char* s, int left, int right) {
    while (left < right) {
        const char temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        left += 1;
        right -= 1;
    }
}

char* reverseStr(char* s, int k) {
    const int length = (int)strlen(s);
    for (int start = 0; start < length; start += 2 * k) {
        int end = start + k - 1;
        if (end >= length) {
            end = length - 1;
        }
        reverse_range(s, start, end);
    }
    return s;
}
