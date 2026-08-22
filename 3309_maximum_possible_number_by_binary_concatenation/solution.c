// LeetCode 3309 - Maximum Possible Number by Binary Concatenation
// https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

#include <stdio.h>
#include <string.h>

static void toBin(int x, char* buf) {
    if (x == 0) { buf[0] = '0'; buf[1] = 0; return; }
    char tmp[40]; int n = 0;
    while (x > 0) { tmp[n++] = (char)('0' + (x & 1)); x >>= 1; }
    for (int i = 0; i < n; i++) buf[i] = tmp[n - 1 - i];
    buf[n] = 0;
}

int maxGoodNumber(int* nums, int numsSize) {
    (void)numsSize;
    char bs[3][40];
    for (int i = 0; i < 3; i++) toBin(nums[i], bs[i]);
    int idx[3] = {0, 1, 2};
    int ans = 0;
    /* generate all permutations */
    int perms[6][3] = {{0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}};
    for (int p = 0; p < 6; p++) {
        char s[120]; s[0] = 0;
        strcat(s, bs[perms[p][0]]);
        strcat(s, bs[perms[p][1]]);
        strcat(s, bs[perms[p][2]]);
        int v = 0;
        for (int i = 0; s[i]; i++) v = v * 2 + (s[i] - '0');
        if (v > ans) ans = v;
    }
    (void)idx;
    return ans;
}
