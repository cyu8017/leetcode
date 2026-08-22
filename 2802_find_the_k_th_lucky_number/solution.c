// LeetCode 2802 - Find The K-th Lucky Number
// https://leetcode.com/problems/find-the-k-th-lucky-number/

#include <stdlib.h>
#include <string.h>

char* kthLuckyNumber(int k) {
    k++;
    char buf[64];
    int len = 0;
    while (k > 1) {
        buf[len++] = (k % 2 == 0) ? '4' : '7';
        k /= 2;
    }
    char* ans = (char*)malloc(len + 1);
    for (int i = 0; i < len; i++) ans[i] = buf[len - 1 - i];
    ans[len] = 0;
    return ans;
}
