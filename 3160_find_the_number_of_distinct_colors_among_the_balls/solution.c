// LeetCode 3160 - Find the Number of Distinct Colors Among the Balls
// https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

#include <stdlib.h>

enum { H3160 = 200003 };
typedef struct { int key, val, used; } E3160;

static int* htget3160(E3160* ht, int key, int create) {
    unsigned h = ((unsigned)key * 2654435761u) % H3160;
    for (int i = 0; i < H3160; i++) {
        unsigned j = (h + i) % H3160;
        if (!ht[j].used) {
            if (!create) return NULL;
            ht[j].used = 1; ht[j].key = key; ht[j].val = 0;
            return &ht[j].val;
        }
        if (ht[j].key == key) return &ht[j].val;
    }
    return NULL;
}

int* queryResults(int limit, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)limit; (void)queriesColSize;
    E3160* g = calloc(H3160, sizeof(E3160));
    E3160* cnt = calloc(H3160, sizeof(E3160));
    int distinct = 0;
    int* ans = malloc(queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        int x = queries[i][0], y = queries[i][1];
        int* cy = htget3160(cnt, y, 1);
        if (*cy == 0) distinct++;
        (*cy)++;
        int* gx = htget3160(g, x, 0);
        if (gx) {
            int v = *gx;
            int* cv = htget3160(cnt, v, 0);
            (*cv)--;
            if (*cv == 0) {
                distinct--;
                /* mark unused - find and clear */
                unsigned h = ((unsigned)v * 2654435761u) % H3160;
                while (cnt[h].key != v) h = (h + 1) % H3160;
                cnt[h].used = 0;
            }
            *gx = y;
        } else {
            *htget3160(g, x, 1) = y;
        }
        ans[i] = distinct;
    }
    free(g); free(cnt);
    *returnSize = queriesSize;
    return ans;
}
