// LeetCode 0888 - Fair Candy Swap
// https://leetcode.com/problems/fair-candy-swap/

#include <stdlib.h>
#include <stdbool.h>

int* fairCandySwap(int* aliceSizes, int aliceSizesSize, int* bobSizes, int bobSizesSize, int* returnSize) {
    int sa = 0, sb = 0;
    bool bob[100001] = {0};
    for (int i = 0; i < aliceSizesSize; i++) sa += aliceSizes[i];
    for (int i = 0; i < bobSizesSize; i++) { sb += bobSizes[i]; bob[bobSizes[i]] = true; }
    int diff = (sa - sb) / 2;
    int* ans = (int*)malloc(2 * sizeof(int));
    for (int i = 0; i < aliceSizesSize; i++) {
        int need = aliceSizes[i] - diff;
        if (need >= 1 && need <= 100000 && bob[need]) {
            ans[0] = aliceSizes[i];
            ans[1] = need;
            *returnSize = 2;
            return ans;
        }
    }
    *returnSize = 0;
    return ans;
}
