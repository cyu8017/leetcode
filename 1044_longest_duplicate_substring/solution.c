// LeetCode 1044 - Longest Duplicate Substring
// https://leetcode.com/problems/longest-duplicate-substring/

#include <stdlib.h>
#include <string.h>

typedef struct {
    unsigned long long h;
    int idx;
    int used;
} HashSlot;

static int search_len(char* s, int n, int length, int* outPos) {
    if (length == 0) { *outPos = 0; return 1; }
    const unsigned long long BASE = 911382323ULL;
    int cap = (n - length + 1) * 2 + 16;
    HashSlot* table = (HashSlot*)calloc((size_t)cap, sizeof(HashSlot));
    unsigned long long h = 0, power = 1;
    for (int i = 0; i < length; i++) {
        h = h * BASE + (unsigned char)s[i];
        if (i) power *= BASE;
    }
    unsigned idx = (unsigned)(h % (unsigned)cap);
    while (table[idx].used) idx = (idx + 1) % (unsigned)cap;
    table[idx].used = 1;
    table[idx].h = h;
    table[idx].idx = 0;

    for (int i = 1; i + length - 1 < n; i++) {
        h = h - (unsigned char)s[i - 1] * power;
        h = h * BASE + (unsigned char)s[i + length - 1];
        idx = (unsigned)(h % (unsigned)cap);
        int found = 0;
        while (table[idx].used) {
            if (table[idx].h == h &&
                strncmp(s + table[idx].idx, s + i, (size_t)length) == 0) {
                *outPos = i;
                found = 1;
                break;
            }
            idx = (idx + 1) % (unsigned)cap;
        }
        if (found) {
            free(table);
            return 1;
        }
        table[idx].used = 1;
        table[idx].h = h;
        table[idx].idx = i;
    }
    free(table);
    return 0;
}

char* longestDupSubstring(char* s) {
    int n = (int)strlen(s);
    int lo = 0, hi = n - 1, bestLen = 0, start = -1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        int pos = -1;
        if (search_len(s, n, mid, &pos)) {
            bestLen = mid;
            start = pos;
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    if (start < 0) {
        char* empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }
    char* ans = (char*)malloc((size_t)bestLen + 1);
    memcpy(ans, s + start, (size_t)bestLen);
    ans[bestLen] = '\0';
    return ans;
}
