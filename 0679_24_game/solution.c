// LeetCode 0679 - 24 Game
// https://leetcode.com/problems/24-game/

#include <math.h>
#include <stdbool.h>

static bool solve(double* nums, int n) {
    if (n == 1) return fabs(nums[0] - 24.0) < 1e-6;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) continue;
            double next[4];
            int idx = 0;
            for (int k = 0; k < n; k++) if (k != i && k != j) next[idx++] = nums[k];
            double candidates[6];
            int c = 0;
            candidates[c++] = nums[i] + nums[j];
            candidates[c++] = nums[i] * nums[j];
            candidates[c++] = nums[i] - nums[j];
            candidates[c++] = nums[j] - nums[i];
            if (fabs(nums[j]) > 1e-9) candidates[c++] = nums[i] / nums[j];
            if (fabs(nums[i]) > 1e-9) candidates[c++] = nums[j] / nums[i];
            for (int t = 0; t < c; t++) {
                next[idx] = candidates[t];
                if (solve(next, idx + 1)) return true;
            }
        }
    }
    return false;
}

bool judgePoint24(int* cards, int cardsSize) {
    double nums[4];
    for (int i = 0; i < cardsSize; i++) nums[i] = cards[i];
    return solve(nums, cardsSize);
}
