// LeetCode 1505 - Minimum Possible Integer After at Most K Adjacent Swaps On Digits
// https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/

#include <stdlib.h>
#include <string.h>

static void fwAdd(int* bit, int n, int i, int delta) {
    for (i++; i <= n; i += i & -i) bit[i] += delta;
}

static int fwSum(int* bit, int i) {
    int out = 0;
    while (i) {
        out += bit[i];
        i -= i & -i;
    }
    return out;
}

char* minInteger(char* num, int k) {
    int n = (int)strlen(num);
    int* pos[10];
    int front[10] = {0}, back[10] = {0};
    for (int d = 0; d < 10; d++) pos[d] = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) {
        int d = num[i] - '0';
        pos[d][back[d]++] = i;
    }
    int* bit = (int*)calloc((size_t)n + 2, sizeof(int));
    char* out = (char*)malloc((size_t)n + 1);
    int oi = 0;
    for (int step = 0; step < n; step++) {
        for (int digit = 0; digit < 10; digit++) {
            if (front[digit] >= back[digit]) continue;
            int index = pos[digit][front[digit]];
            int cost = index - fwSum(bit, index);
            if (cost <= k) {
                k -= cost;
                front[digit]++;
                fwAdd(bit, n, index, 1);
                out[oi++] = (char)('0' + digit);
                break;
            }
        }
    }
    out[oi] = '\0';
    for (int d = 0; d < 10; d++) free(pos[d]);
    free(bit);
    return out;
}
