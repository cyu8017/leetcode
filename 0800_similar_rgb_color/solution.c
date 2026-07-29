// LeetCode 0800 - Similar RGB Color
// https://leetcode.com/problems/similar-rgb-color/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int hexVal(char c) {
    if (c >= '0' && c <= '9') return c - '0';
    return c - 'a' + 10;
}

static void closest(const char* component, char* out) {
    int value = hexVal(component[0]) * 16 + hexVal(component[1]);
    int rounded = (value + 8) / 17;
    sprintf(out, "%x%x", rounded, rounded);
}

char* similarRGB(char* color) {
    char* ans = (char*)malloc(8);
    ans[0] = '#';
    closest(color + 1, ans + 1);
    closest(color + 3, ans + 3);
    closest(color + 5, ans + 5);
    ans[7] = '\0';
    return ans;
}
