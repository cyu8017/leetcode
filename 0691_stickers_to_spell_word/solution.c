// LeetCode 0691 - Stickers to Spell Word
// https://leetcode.com/problems/stickers-to-spell-word/

#include <limits.h>
#include <stdlib.h>
#include <string.h>

static int dfs(int* need, int* chars, int nChars, int sticks[][26], int stickCount, int* memo, int memoSize) {
    int key = 0;
    for (int i = 0; i < nChars; i++) key = key * 7 + need[i];
    if (key < memoSize && memo[key] >= 0) return memo[key];
    int i = 0;
    while (i < nChars && need[i] == 0) i++;
    if (i == nChars) return 0;
    int best = INT_MAX / 2;
    for (int s = 0; s < stickCount; s++) {
        if (sticks[s][chars[i]] == 0) continue;
        int nxt[16];
        for (int j = 0; j < nChars; j++) {
            int rem = need[j] - sticks[s][chars[j]];
            nxt[j] = rem > 0 ? rem : 0;
        }
        int cand = 1 + dfs(nxt, chars, nChars, sticks, stickCount, memo, memoSize);
        if (cand < best) best = cand;
    }
    if (key < memoSize) memo[key] = best;
    return best;
}

int minStickers(char** stickers, int stickersSize, char* target) {
    int needMap[26] = {0};
    for (char* p = target; *p; p++) needMap[*p - 'a']++;
    int chars[26], nChars = 0;
    for (int i = 0; i < 26; i++) if (needMap[i]) chars[nChars++] = i;
    int sticks[50][26];
    int stickCount = 0;
    for (int s = 0; s < stickersSize; s++) {
        int counts[26] = {0};
        for (char* p = stickers[s]; *p; p++) counts[*p - 'a']++;
        int useful = 0;
        memset(sticks[stickCount], 0, sizeof(sticks[stickCount]));
        for (int i = 0; i < nChars; i++) {
            if (counts[chars[i]]) {
                sticks[stickCount][chars[i]] = counts[chars[i]];
                useful = 1;
            }
        }
        if (useful) stickCount++;
    }
    int need[16];
    for (int i = 0; i < nChars; i++) need[i] = needMap[chars[i]];
    int memoSize = 1;
    for (int i = 0; i < nChars; i++) memoSize *= 7;
    int* memo = (int*)malloc((size_t)memoSize * sizeof(int));
    for (int i = 0; i < memoSize; i++) memo[i] = -1;
    int result = dfs(need, chars, nChars, sticks, stickCount, memo, memoSize);
    free(memo);
    return result >= INT_MAX / 4 ? -1 : result;
}
