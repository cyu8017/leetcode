// LeetCode 0822 - Card Flipping Game
// https://leetcode.com/problems/card-flipping-game/

#include <stdbool.h>

#define MIN(a,b) ((a)<(b)?(a):(b))

int flipgame(int* fronts, int frontsSize, int* backs, int backsSize) {
    (void)backsSize;
    bool same[2001] = {0};
    for (int i = 0; i < frontsSize; i++)
        if (fronts[i] == backs[i]) same[fronts[i]] = true;
    int best = 2001;
    for (int i = 0; i < frontsSize; i++) {
        if (!same[fronts[i]]) best = MIN(best, fronts[i]);
        if (!same[backs[i]]) best = MIN(best, backs[i]);
    }
    return best == 2001 ? 0 : best;
}
