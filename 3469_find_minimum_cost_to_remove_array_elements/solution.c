// LeetCode 3469 - Find Minimum Cost to Remove Array Elements
// https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/

#include <stdlib.h>
#include <string.h>

static int* nums3469;
static int n3469;
static int* memo3469;

static int max2_3469(int a, int b) { return a > b ? a : b; }
static int min3_3469(int a, int b, int c) {
    if (a > b) a = b;
    if (a > c) a = c;
    return a;
}

static int dfs3469(int i, int prev) {
    if (i >= n3469) return prev == -1 ? 0 : nums3469[prev];
    int key = i * (n3469 + 1) + (prev + 1);
    if (memo3469[key] != -1) return memo3469[key];
    int res;
    if (prev == -1) {
        if (i + 1 >= n3469) res = nums3469[i];
        else if (i + 2 >= n3469) res = max2_3469(nums3469[i], nums3469[i + 1]);
        else {
            int a = nums3469[i], b = nums3469[i + 1], c = nums3469[i + 2];
            res = min3_3469(
                max2_3469(b, c) + dfs3469(i + 3, i),
                max2_3469(a, c) + dfs3469(i + 3, i + 1),
                max2_3469(a, b) + dfs3469(i + 3, i + 2));
        }
    } else {
        if (i + 1 >= n3469) res = max2_3469(nums3469[prev], nums3469[i]);
        else {
            int a = nums3469[prev], b = nums3469[i], c = nums3469[i + 1];
            res = min3_3469(
                max2_3469(b, c) + dfs3469(i + 2, prev),
                max2_3469(a, c) + dfs3469(i + 2, i),
                max2_3469(a, b) + dfs3469(i + 2, i + 1));
        }
    }
    memo3469[key] = res;
    return res;
}

int minCost(int* nums, int numsSize) {
    nums3469 = nums;
    n3469 = numsSize;
    int msz = (numsSize + 1) * (numsSize + 1);
    memo3469 = (int*)malloc((size_t)msz * sizeof(int));
    for (int i = 0; i < msz; i++) memo3469[i] = -1;
    int ans = dfs3469(0, -1);
    free(memo3469);
    return ans;
}
