// LeetCode 3984 - Divisible Game
// https://leetcode.com/problems/divisible-game/

#include <stdlib.h>

int divisibleGame(int* nums, int numsSize) {
    int* cand = (int*)malloc((size_t)(numsSize * 64 + 8) * sizeof(int));
    int candCnt = 0;
    cand[candCnt++] = 2;

    for (int ii = 0; ii < numsSize; ii++) {
        int value = nums[ii];
        for (int divisor = 2; divisor * divisor <= value; divisor++) {
            if (value % divisor != 0) continue;
            cand[candCnt++] = divisor;
            cand[candCnt++] = value / divisor;
        }
        if (value > 1) cand[candCnt++] = value;
    }

    /* unique candidates */
    for (int i = 0; i < candCnt; i++) {
        for (int j = i + 1; j < candCnt; ) {
            if (cand[j] == cand[i]) {
                cand[j] = cand[--candCnt];
            } else j++;
        }
    }

    long long bestScore = -(1LL << 62);
    int bestK = 0;
    for (int ci = 0; ci < candCnt; ci++) {
        int k = cand[ci];
        long long ending = 0, score = 0;
        for (int i = 0; i < numsSize; i++) {
            int value = nums[i];
            long long contribution = -((long long)value);
            if (value % k == 0) contribution = value;
            if (i == 0 || ending + contribution < contribution) ending = contribution;
            else ending += contribution;
            if (i == 0 || ending > score) score = ending;
        }
        if (score > bestScore || (score == bestScore && k < bestK)) {
            bestScore = score;
            bestK = k;
        }
    }
    free(cand);

    const long long mod = 1000000007LL;
    long long answer = (bestScore % mod) * bestK % mod;
    if (answer < 0) answer += mod;
    return (int)answer;
}
