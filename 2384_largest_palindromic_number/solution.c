// LeetCode 2384 - Largest Palindromic Number
// https://leetcode.com/problems/largest-palindromic-number/

#include <stdlib.h>
#include <string.h>

char* largestPalindromic(char* num) {
    int cnt[10] = {0};
    for (int i = 0; num[i]; i++) cnt[num[i] - '0']++;
    char left[100001]; int ln = 0;
    for (int d = 9; d >= 0; d--) {
        while (cnt[d] >= 2) {
            if (d == 0 && ln == 0) break;
            left[ln++] = (char)('0' + d);
            cnt[d] -= 2;
        }
    }
    char mid = 0;
    for (int d = 9; d >= 0; d--) if (cnt[d] > 0) { mid = (char)('0' + d); break; }
    char* res;
    if (ln == 0) {
        res = (char*)malloc(2);
        res[0] = mid ? mid : '0';
        res[1] = '\0';
        return res;
    }
    int total = ln * 2 + (mid ? 1 : 0);
    res = (char*)malloc((size_t)(total + 1));
    memcpy(res, left, (size_t)ln);
    int p = ln;
    if (mid) res[p++] = mid;
    for (int i = ln - 1; i >= 0; i--) res[p++] = left[i];
    res[p] = '\0';
    return res;
}
