// LeetCode 1774 - Closest Dessert Cost
// https://leetcode.com/problems/closest-dessert-cost/

#include <stdlib.h>

static void dfs(int i, int cur, int target, const int* toppingCosts, int toppingCostsSize,
                int* best) {
    int curDiff = abs(cur - target);
    int bestDiff = abs(*best - target);
    if (curDiff < bestDiff || (curDiff == bestDiff && cur < *best)) {
        *best = cur;
    }
    if (i == toppingCostsSize || cur >= target) {
        return;
    }
    dfs(i + 1, cur, target, toppingCosts, toppingCostsSize, best);
    dfs(i + 1, cur + toppingCosts[i], target, toppingCosts, toppingCostsSize, best);
    dfs(i + 1, cur + 2 * toppingCosts[i], target, toppingCosts, toppingCostsSize, best);
}

int closestCost(int* baseCosts, int baseCostsSize, int* toppingCosts, int toppingCostsSize,
                int target) {
    int best = 1 << 29;
    for (int b = 0; b < baseCostsSize; b++) {
        dfs(0, baseCosts[b], target, toppingCosts, toppingCostsSize, &best);
    }
    return best;
}
