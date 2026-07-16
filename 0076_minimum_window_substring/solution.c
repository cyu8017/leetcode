// LeetCode 0076 - Minimum Window Substring
// https://leetcode.com/problems/minimum-window-substring/

#include <limits.h>
#include <stdlib.h>
#include <string.h>

char* minWindow(char* s, char* t) {
    int tLen = (int)strlen(t);
    if (tLen == 0) {
        char* empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }

    int need[256] = {0};
    int required = 0;
    for (int i = 0; i < tLen; i++) {
        unsigned char ch = (unsigned char)t[i];
        if (need[ch] == 0) {
            required++;
        }
        need[ch]++;
    }

    int window[256] = {0};
    int formed = 0;
    int left = 0;
    int sLen = (int)strlen(s);
    int bestLen = INT_MAX;
    int bestLeft = 0;

    for (int right = 0; right < sLen; right++) {
        unsigned char ch = (unsigned char)s[right];
        window[ch]++;
        if (need[ch] > 0 && window[ch] == need[ch]) {
            formed++;
        }

        while (formed == required) {
            if (right - left + 1 < bestLen) {
                bestLen = right - left + 1;
                bestLeft = left;
            }

            unsigned char leftCh = (unsigned char)s[left];
            window[leftCh]--;
            if (need[leftCh] > 0 && window[leftCh] < need[leftCh]) {
                formed--;
            }
            left++;
        }
    }

    if (bestLen == INT_MAX) {
        char* empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }

    char* result = (char*)malloc((size_t)bestLen + 1);
    memcpy(result, s + bestLeft, (size_t)bestLen);
    result[bestLen] = '\0';
    return result;
}
