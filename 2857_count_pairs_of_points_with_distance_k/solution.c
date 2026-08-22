// LeetCode 2857 - Count Pairs of Points With Distance k
// https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

#include <stdlib.h>

typedef struct { long long key; int cnt; int used; } E;
static long long mk(int x, int y) { return ((long long)x << 32) ^ (unsigned)y; }

int countPairs(int** coordinates, int coordinatesSize, int* coordinatesColSize, int k) {
    (void)coordinatesColSize;
    int htsz = 1;
    while (htsz < coordinatesSize * 4 + 16) htsz <<= 1;
    E* ht = (E*)calloc(htsz, sizeof(E));
    int ans = 0;
    for (int i = 0; i < coordinatesSize; i++) {
        int x = coordinates[i][0], y = coordinates[i][1];
        for (int a = 0; a <= k; a++) {
            int b = k - a;
            long long key = mk(x ^ a, y ^ b);
            unsigned h = (unsigned)(key & (htsz - 1));
            while (ht[h].used && ht[h].key != key) h = (h + 1) & (htsz - 1);
            if (ht[h].used) ans += ht[h].cnt;
        }
        long long key = mk(x, y);
        unsigned h = (unsigned)(key & (htsz - 1));
        while (ht[h].used && ht[h].key != key) h = (h + 1) & (htsz - 1);
        if (!ht[h].used) { ht[h].used = 1; ht[h].key = key; ht[h].cnt = 0; }
        ht[h].cnt++;
    }
    free(ht);
    return ans;
}
