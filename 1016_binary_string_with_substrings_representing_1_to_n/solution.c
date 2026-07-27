// LeetCode 1016 - Binary String With Substrings Representing 1 To N
// https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

#include <stdbool.h>
#include <string.h>

static void int_to_bin(int x, char* buf) {
    char tmp[40];
    int len = 0;
    while (x) {
        tmp[len++] = (char)('0' + (x & 1));
        x >>= 1;
    }
    for (int i = 0; i < len; i++) buf[i] = tmp[len - 1 - i];
    buf[len] = '\0';
}

bool queryString(char* s, int n) {
    char bin[40];
    for (int i = n; i > n / 2; i--) {
        int_to_bin(i, bin);
        if (!strstr(s, bin)) return false;
    }
    return true;
}
