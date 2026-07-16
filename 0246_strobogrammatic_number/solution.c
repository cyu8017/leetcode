// LeetCode 0246 - Strobogrammatic Number
// https://leetcode.com/problems/strobogrammatic-number/

#include <stdbool.h>
#include <string.h>

static char strobogrammatic_match(char c) {
    switch (c) {
        case '0': return '0';
        case '1': return '1';
        case '6': return '9';
        case '8': return '8';
        case '9': return '6';
        default: return '\0';
    }
}

bool isStrobogrammatic(char* num) {
    int left = 0;
    int right = (int)strlen(num) - 1;
    while (left <= right) {
        if (strobogrammatic_match(num[left]) != num[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
