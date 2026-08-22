// LeetCode 2768 - Number of Black Blocks
// https://leetcode.com/problems/number-of-black-blocks/

#include <stdlib.h>

typedef struct { long long key; int cnt; int used; } Entry;

static long long mk(int i, int j) { return ((long long)i << 32) ^ (unsigned)j; }

long long* countBlackBlocks(int m, int n, int** coordinates, int coordinatesSize, int* coordinatesColSize, int* returnSize) {
    (void)coordinatesColSize;
    int cap = coordinatesSize * 4 + 16;
    if (cap < 16) cap = 16;
    Entry* ht = (Entry*)calloc(cap * 2, sizeof(Entry));
    int htsz = cap * 2;
    for (int c = 0; c < coordinatesSize; c++) {
        int x = coordinates[c][0], y = coordinates[c][1];
        for (int i = x - 1; i <= x; i++) {
            for (int j = y - 1; j <= y; j++) {
                if (i >= 0 && j >= 0 && i < m - 1 && j < n - 1) {
                    long long key = mk(i, j);
                    unsigned h = (unsigned)(key % htsz);
                    while (ht[h].used && ht[h].key != key) h = (h + 1) % htsz;
                    if (!ht[h].used) { ht[h].used = 1; ht[h].key = key; ht[h].cnt = 0; }
                    ht[h].cnt++;
                }
            }
        }
    }
    long long* ans = (long long*)calloc(5, sizeof(long long));
    ans[0] = (long long)(m - 1) * (n - 1);
    for (int i = 0; i < htsz; i++) {
        if (ht[i].used) {
            ans[ht[i].cnt]++;
            ans[0]--;
        }
    }
    free(ht);
    *returnSize = 5;
    return ans;
}
