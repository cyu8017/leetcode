// LeetCode 3205 - Maximum Array Hopping Score I
// https://leetcode.com/problems/maximum-array-hopping-score-i/

#include <stdlib.h>
#include <string.h>

static int *nums3205, n3205, *f3205;

static int dfs3205(int i) {
    if (f3205[i] > 0) return f3205[i];
    for (int j = i + 1; j < n3205; j++) {
        int v = (j - i) * nums3205[j] + dfs3205(j);
        if (v > f3205[i]) f3205[i] = v;
    }
    return f3205[i];
}

int maxScore(int* nums, int numsSize) {
    nums3205 = nums; n3205 = numsSize;
    f3205 = calloc(n3205, sizeof(int));
    int ans = dfs3205(0);
    free(f3205);
    return ans;
}
