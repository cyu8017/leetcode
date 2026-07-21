// LeetCode 1900 - The Earliest and Latest Rounds Where Players Compete
// https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

#include <limits.h>
#include <stdlib.h>
#include <string.h>

static int g_first;
static int g_second;

typedef struct {
    int* players;
    int count;
    int early;
    int late;
    int used;
} MemoEntry;

static MemoEntry* g_memo;
static int g_memoSize;
static int g_memoCap;

static int playersEqual(const int* a, int an, const int* b, int bn) {
    if (an != bn) return 0;
    for (int i = 0; i < an; i++) if (a[i] != b[i]) return 0;
    return 1;
}

static int findMemo(const int* players, int count) {
    for (int i = 0; i < g_memoSize; i++) {
        if (g_memo[i].used && playersEqual(g_memo[i].players, g_memo[i].count, players, count)) {
            return i;
        }
    }
    return -1;
}

static void storeMemo(const int* players, int count, int early, int late) {
    if (g_memoSize == g_memoCap) {
        g_memoCap = g_memoCap ? g_memoCap * 2 : 64;
        g_memo = (MemoEntry*)realloc(g_memo, (size_t)g_memoCap * sizeof(MemoEntry));
    }
    MemoEntry* e = &g_memo[g_memoSize++];
    e->players = (int*)malloc((size_t)count * sizeof(int));
    memcpy(e->players, players, (size_t)count * sizeof(int));
    e->count = count;
    e->early = early;
    e->late = late;
    e->used = 1;
}

static int cmpAsc(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static void dfs(int* players, int count, int* earlyOut, int* lateOut);

static void enumerate(int** choices, int* choiceSizes, int choiceCount, int idx, int* picks,
                      int pickCount, int* earliest, int* latest) {
    if (idx == choiceCount) {
        int* winners = (int*)malloc((size_t)pickCount * sizeof(int));
        memcpy(winners, picks, (size_t)pickCount * sizeof(int));
        qsort(winners, (size_t)pickCount, sizeof(int), cmpAsc);
        int early = 0, late = 0;
        dfs(winners, pickCount, &early, &late);
        if (early + 1 < *earliest) *earliest = early + 1;
        if (late + 1 > *latest) *latest = late + 1;
        free(winners);
        return;
    }
    for (int i = 0; i < choiceSizes[idx]; i++) {
        picks[pickCount] = choices[idx][i];
        enumerate(choices, choiceSizes, choiceCount, idx + 1, picks, pickCount + 1, earliest, latest);
    }
}

static void dfs(int* players, int count, int* earlyOut, int* lateOut) {
    int memoIdx = findMemo(players, count);
    if (memoIdx >= 0) {
        *earlyOut = g_memo[memoIdx].early;
        *lateOut = g_memo[memoIdx].late;
        return;
    }

    int firstIndex = -1, secondIndex = -1;
    for (int i = 0; i < count; i++) {
        if (players[i] == g_first) firstIndex = i;
        if (players[i] == g_second) secondIndex = i;
    }
    if (firstIndex + secondIndex == count - 1) {
        storeMemo(players, count, 1, 1);
        *earlyOut = 1;
        *lateOut = 1;
        return;
    }

    int choiceCap = count / 2 + 1;
    int** choices = (int**)malloc((size_t)choiceCap * sizeof(int*));
    int* choiceSizes = (int*)malloc((size_t)choiceCap * sizeof(int));
    int choiceCount = 0;
    for (int index = 0; index < count / 2; index++) {
        int left = players[index];
        int right = players[count - 1 - index];
        choices[choiceCount] = (int*)malloc(2 * sizeof(int));
        if (left == g_first || left == g_second) {
            choices[choiceCount][0] = left;
            choiceSizes[choiceCount] = 1;
        } else if (right == g_first || right == g_second) {
            choices[choiceCount][0] = right;
            choiceSizes[choiceCount] = 1;
        } else {
            choices[choiceCount][0] = left;
            choices[choiceCount][1] = right;
            choiceSizes[choiceCount] = 2;
        }
        choiceCount++;
    }
    if (count % 2) {
        choices[choiceCount] = (int*)malloc(sizeof(int));
        choices[choiceCount][0] = players[count / 2];
        choiceSizes[choiceCount] = 1;
        choiceCount++;
    }

    int earliest = INT_MAX;
    int latest = 0;
    int* picks = (int*)malloc((size_t)choiceCount * sizeof(int));
    enumerate(choices, choiceSizes, choiceCount, 0, picks, 0, &earliest, &latest);

    for (int i = 0; i < choiceCount; i++) free(choices[i]);
    free(choices);
    free(choiceSizes);
    free(picks);

    storeMemo(players, count, earliest, latest);
    *earlyOut = earliest;
    *lateOut = latest;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* earliestAndLatest(int n, int firstPlayer, int secondPlayer, int* returnSize) {
    g_first = firstPlayer;
    g_second = secondPlayer;
    g_memo = NULL;
    g_memoSize = 0;
    g_memoCap = 0;

    int* players = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) players[i] = i + 1;
    int early = 0, late = 0;
    dfs(players, n, &early, &late);

    int* result = (int*)malloc(2 * sizeof(int));
    result[0] = early;
    result[1] = late;
    *returnSize = 2;

    for (int i = 0; i < g_memoSize; i++) free(g_memo[i].players);
    free(g_memo);
    free(players);
    return result;
}
