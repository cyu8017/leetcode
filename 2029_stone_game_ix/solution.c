// LeetCode 2029 - Stone Game IX
// https://leetcode.com/problems/stone-game-ix/

#include <stdbool.h>
#include <stdlib.h>

bool stoneGameIX(int* stones, int stonesSize) {
    int cnt[3] = {0};
    for (int i = 0; i < stonesSize; i++) cnt[stones[i] % 3]++;
    if (cnt[0] % 2 == 0) return cnt[1] > 0 && cnt[2] > 0;
    return abs(cnt[1] - cnt[2]) > 2;
}
