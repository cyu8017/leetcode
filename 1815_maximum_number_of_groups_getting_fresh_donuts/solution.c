// LeetCode 1815 - Maximum Number of Groups Getting Fresh Donuts
// https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/

#include <stdlib.h>
#include <string.h>

typedef struct {
    unsigned long long key;
    int value;
    int used;
} MemoEntry;

static MemoEntry* memo;
static int memoCap;
static int batchSz;
static int* counts;

static int memoGet(unsigned long long key, int* found) {
    unsigned long long idx = key % (unsigned long long)memoCap;
    while (memo[idx].used) {
        if (memo[idx].key == key) {
            *found = 1;
            return memo[idx].value;
        }
        idx = (idx + 1) % (unsigned long long)memoCap;
    }
    *found = 0;
    return 0;
}

static void memoPut(unsigned long long key, int value) {
    unsigned long long idx = key % (unsigned long long)memoCap;
    while (memo[idx].used) {
        if (memo[idx].key == key) {
            memo[idx].value = value;
            return;
        }
        idx = (idx + 1) % (unsigned long long)memoCap;
    }
    memo[idx].used = 1;
    memo[idx].key = key;
    memo[idx].value = value;
}

static unsigned long long encodeState(int remainder) {
    unsigned long long state = 0;
    unsigned long long base = 1;
    for (int mod = 1; mod < batchSz; mod++) {
        state += (unsigned long long)counts[mod] * base;
        base *= 31ULL;
    }
    return state * (unsigned long long)batchSz + (unsigned long long)remainder;
}

static int dfs(int remainder) {
    unsigned long long key = encodeState(remainder);
    int found = 0;
    int cached = memoGet(key, &found);
    if (found) return cached;

    int best = 0;
    for (int mod = 1; mod < batchSz; mod++) {
        if (counts[mod] == 0) continue;
        counts[mod]--;
        int cur = dfs((remainder + mod) % batchSz);
        if (cur > best) best = cur;
        counts[mod]++;
    }
    if (remainder == 0) best += 1;
    memoPut(key, best);
    return best;
}

int maxHappyGroups(int batchSize, int* groups, int groupsSize) {
    batchSz = batchSize;
    counts = (int*)calloc((size_t)batchSize, sizeof(int));
    for (int i = 0; i < groupsSize; i++) counts[groups[i] % batchSize]++;

    memoCap = 1 << 22;
    memo = (MemoEntry*)calloc((size_t)memoCap, sizeof(MemoEntry));

    int ans = dfs(0);
    if (counts[0]) ans += counts[0] - 1;

    free(memo);
    free(counts);
    memo = NULL;
    counts = NULL;
    return ans;
}
