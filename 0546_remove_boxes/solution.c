// LeetCode 0546 - Remove Boxes
// https://leetcode.com/problems/remove-boxes/

#include <stdlib.h>

static int maxInt(int left, int right) {
    return left > right ? left : right;
}

static int dp(
    int left,
    int right,
    int streak,
    int* boxes,
    int n,
    int*** memo) {
    if (left > right) {
        return 0;
    }
    if (memo[left][right][streak] >= 0) {
        return memo[left][right][streak];
    }

    while (right > left && boxes[right] == boxes[right - 1]) {
        right -= 1;
        streak += 1;
    }

    int best = (streak + 1) * (streak + 1) + dp(left, right - 1, 0, boxes, n, memo);
    for (int index = left; index < right; index++) {
        if (boxes[index] == boxes[right]) {
            const int candidate = dp(left, index, streak + 1, boxes, n, memo) +
                                  dp(index + 1, right - 1, 0, boxes, n, memo);
            best = maxInt(best, candidate);
        }
    }

    memo[left][right][streak] = best;
    return best;
}

int removeBoxes(int* boxes, int boxesSize) {
    const int n = boxesSize;
    int*** memo = (int***)malloc((size_t)n * sizeof(int**));
    for (int left = 0; left < n; left++) {
        memo[left] = (int**)malloc((size_t)n * sizeof(int*));
        for (int right = 0; right < n; right++) {
            memo[left][right] = (int*)malloc((size_t)(n + 1) * sizeof(int));
            for (int streak = 0; streak <= n; streak++) {
                memo[left][right][streak] = -1;
            }
        }
    }

    const int result = dp(0, n - 1, 0, boxes, n, memo);

    for (int left = 0; left < n; left++) {
        for (int right = 0; right < n; right++) {
            free(memo[left][right]);
        }
        free(memo[left]);
    }
    free(memo);
    return result;
}
