// LeetCode 2060 - Check if an Original String Exists Given Two Encoded Strings
// https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/

#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

typedef struct { int i, j, diff; int used; bool val; } Memo2060;

static Memo2060* memo2060;
static int memoCap2060;
static const char *s1_2060, *s2_2060;
static int n2060, m2060;

static unsigned h2060(int i, int j, int diff) {
    return (unsigned)i * 131u + (unsigned)j * 137u + (unsigned)(diff + 2000) * 149u;
}

static bool* memoGet(int i, int j, int diff, bool* found) {
    int idx = (int)(h2060(i, j, diff) & (unsigned)(memoCap2060 - 1));
    for (;;) {
        if (!memo2060[idx].used) {
            *found = false;
            memo2060[idx].used = 1;
            memo2060[idx].i = i; memo2060[idx].j = j; memo2060[idx].diff = diff;
            return &memo2060[idx].val;
        }
        if (memo2060[idx].i == i && memo2060[idx].j == j && memo2060[idx].diff == diff) {
            *found = true;
            return &memo2060[idx].val;
        }
        idx = (idx + 1) & (memoCap2060 - 1);
    }
}

static bool dfs2060(int i, int j, int diff) {
    bool found;
    bool* slot = memoGet(i, j, diff, &found);
    if (found) return *slot;
    if (i == n2060 && j == m2060) { *slot = (diff == 0); return *slot; }
    bool res = false;
    if (diff == 0 && i < n2060 && j < m2060 &&
        (s1_2060[i] < '0' || s1_2060[i] > '9') && (s2_2060[j] < '0' || s2_2060[j] > '9')) {
        if (s1_2060[i] == s2_2060[j]) res = dfs2060(i + 1, j + 1, 0);
    } else if (diff > 0 && i < n2060 && (s1_2060[i] < '0' || s1_2060[i] > '9')) {
        res = dfs2060(i + 1, j, diff - 1);
    } else if (diff < 0 && j < m2060 && (s2_2060[j] < '0' || s2_2060[j] > '9')) {
        res = dfs2060(i, j + 1, diff + 1);
    }
    if (!res && i < n2060 && s1_2060[i] >= '0' && s1_2060[i] <= '9') {
        int val = 0;
        for (int p = i; p < n2060 && s1_2060[p] >= '0' && s1_2060[p] <= '9'; p++) {
            val = val * 10 + (s1_2060[p] - '0');
            if (dfs2060(p + 1, j, diff + val)) { res = true; break; }
        }
    }
    if (!res && j < m2060 && s2_2060[j] >= '0' && s2_2060[j] <= '9') {
        int val = 0;
        for (int p = j; p < m2060 && s2_2060[p] >= '0' && s2_2060[p] <= '9'; p++) {
            val = val * 10 + (s2_2060[p] - '0');
            if (dfs2060(i, p + 1, diff - val)) { res = true; break; }
        }
    }
    *slot = res;
    return res;
}

bool possiblyEquals(char* s1, char* s2) {
    s1_2060 = s1; s2_2060 = s2;
    n2060 = (int)strlen(s1); m2060 = (int)strlen(s2);
    memoCap2060 = 1 << 16;
    memo2060 = (Memo2060*)calloc((size_t)memoCap2060, sizeof(Memo2060));
    bool ans = dfs2060(0, 0, 0);
    free(memo2060);
    return ans;
}
