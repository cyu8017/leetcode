// LeetCode 1340 - Jump Game V
// https://leetcode.com/problems/jump-game-v/

#include <stdlib.h>

typedef struct { int value, idx; } Item;
static int cmp_item(const void* a, const void* b) {
    const Item* x = (const Item*)a;
    const Item* y = (const Item*)b;
    if (x->value != y->value) return x->value - y->value;
    return x->idx - y->idx;
}

int maxJumps(int* arr, int arrSize, int d) {
    int* dp = (int*)malloc(arrSize * sizeof(int));
    Item* items = (Item*)malloc(arrSize * sizeof(Item));
    for (int i = 0; i < arrSize; i++) {
        dp[i] = 1;
        items[i].value = arr[i];
        items[i].idx = i;
    }
    qsort(items, arrSize, sizeof(Item), cmp_item);
    for (int t = 0; t < arrSize; t++) {
        int i = items[t].idx;
        for (int step = -1; step <= 1; step += 2) {
            int j = i + step;
            while (j >= 0 && j < arrSize && (j > i ? j - i : i - j) <= d && arr[j] < arr[i]) {
                if (1 + dp[j] > dp[i]) dp[i] = 1 + dp[j];
                j += step;
            }
        }
    }
    int ans = 0;
    for (int i = 0; i < arrSize; i++) if (dp[i] > ans) ans = dp[i];
    free(dp); free(items);
    return ans;
}
