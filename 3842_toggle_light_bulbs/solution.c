// LeetCode 3842 - Toggle Light Bulbs
// https://leetcode.com/problems/toggle-light-bulbs/

#include <stdlib.h>

int* toggleLightBulbs(int* bulbs, int bulbsSize, int* returnSize) {
    int st[101] = {0};
    for (int i = 0; i < bulbsSize; i++) st[bulbs[i]] ^= 1;
    int* ans = (int*)malloc(101 * sizeof(int));
    int asz = 0;
    for (int i = 0; i < 101; i++) if (st[i] == 1) ans[asz++] = i;
    *returnSize = asz;
    return ans;
}
