// LeetCode 1652 - Defuse the Bomb
// https://leetcode.com/problems/defuse-the-bomb/

#include <stdlib.h>

int* decrypt(int* code, int codeSize, int k, int* returnSize) {
    int* ans = (int*)calloc((size_t)codeSize, sizeof(int));
    *returnSize = codeSize;
    if (k == 0) return ans;
    for (int i = 0; i < codeSize; i++) {
        int sum = 0;
        if (k > 0) {
            for (int j = 1; j <= k; j++) sum += code[(i + j) % codeSize];
        } else {
            for (int j = 1; j <= -k; j++) sum += code[(i - j + codeSize * 100) % codeSize];
        }
        ans[i] = sum;
    }
    return ans;
}
