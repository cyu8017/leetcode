// LeetCode 2042 - Check if Numbers Are Ascending in a Sentence
// https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

#include <stdbool.h>
#include <stdlib.h>

bool areNumbersAscending(char* s) {
    int prev = -1;
    char* p = s;
    while (*p) {
        while (*p == ' ') p++;
        if (!*p) break;
        if (*p >= '0' && *p <= '9') {
            int v = 0;
            while (*p >= '0' && *p <= '9') { v = v * 10 + (*p - '0'); p++; }
            if (v <= prev) return false;
            prev = v;
        } else {
            while (*p && *p != ' ') p++;
        }
    }
    return true;
}
