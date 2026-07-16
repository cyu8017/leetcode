// LeetCode 0514 - Freedom Trail
// https://leetcode.com/problems/freedom-trail/

#include <limits.h>
#include <string.h>

#define MAX_POSITIONS 100

static int positions[26][MAX_POSITIONS];
static int posCounts[26];
static int memo[101][101];

static int dp(int ringIndex, int keyIndex, const char* ring, const char* key, int ringLen, int keyLen) {
    if (keyIndex == keyLen) {
        return 0;
    }
    if (memo[ringIndex][keyIndex] != -1) {
        return memo[ringIndex][keyIndex];
    }

    int best = INT_MAX;
    const int charIndex = key[keyIndex] - 'a';
    for (int posIndex = 0; posIndex < posCounts[charIndex]; posIndex++) {
        const int pos = positions[charIndex][posIndex];
        const int clockwise = (pos - ringIndex + ringLen) % ringLen;
        const int counter = (ringIndex - pos + ringLen) % ringLen;
        const int steps = (clockwise < counter ? clockwise : counter) + 1;
        const int candidate = steps + dp(pos, keyIndex + 1, ring, key, ringLen, keyLen);
        if (candidate < best) {
            best = candidate;
        }
    }
    memo[ringIndex][keyIndex] = best;
    return best;
}

int findRotateSteps(char* ring, char* key) {
    memset(posCounts, 0, sizeof(posCounts));
    const int ringLen = (int)strlen(ring);
    const int keyLen = (int)strlen(key);
    for (int index = 0; index < ringLen; index++) {
        const int charIndex = ring[index] - 'a';
        positions[charIndex][posCounts[charIndex]++] = index;
    }
    for (int ringIndex = 0; ringIndex <= ringLen; ringIndex++) {
        for (int keyIndex = 0; keyIndex <= keyLen; keyIndex++) {
            memo[ringIndex][keyIndex] = -1;
        }
    }
    return dp(0, 0, ring, key, ringLen, keyLen);
}
