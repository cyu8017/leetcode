// LeetCode 2564 - Substring XOR Queries
// https://leetcode.com/problems/substring-xor-queries/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct { int key; int l, r; bool set; } Pos;

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** substringXorQueries(char* s, int** queries, int queriesSize, int* queriesColSize, int* returnSize, int** returnColumnSizes) {
    (void)queriesColSize;
    int n = (int)strlen(s);
    // hash map open addressing for values up to ~2^30
    int cap = 1 << 20;
    Pos* pos = (Pos*)calloc((size_t)cap, sizeof(Pos));
    #define PUT(v, L, R) do { \
        unsigned h = (unsigned)(v) & (cap - 1); \
        while (pos[h].set && pos[h].key != (v)) h = (h + 1) & (cap - 1); \
        if (!pos[h].set) { pos[h].set = true; pos[h].key = (v); pos[h].l = (L); pos[h].r = (R); } \
    } while (0)
    #define GET(v, outL, outR, ok) do { \
        unsigned h = (unsigned)(v) & (cap - 1); \
        (ok) = 0; \
        while (pos[h].set) { \
            if (pos[h].key == (v)) { (outL)=pos[h].l; (outR)=pos[h].r; (ok)=1; break; } \
            h = (h + 1) & (cap - 1); \
        } \
    } while (0)

    for (int i = 0; i < n; i++) {
        if (s[i] == '0') { PUT(0, i, i); continue; }
        int val = 0;
        for (int j = i; j < n && j < i + 30; j++) {
            val = val * 2 + (s[j] - '0');
            PUT(val, i, j);
        }
    }
    int** ans = (int**)malloc((size_t)queriesSize * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        ans[i] = (int*)malloc(2 * sizeof(int));
        (*returnColumnSizes)[i] = 2;
        int need = queries[i][0] ^ queries[i][1];
        int L, R, ok;
        GET(need, L, R, ok);
        if (ok) { ans[i][0] = L; ans[i][1] = R; }
        else { ans[i][0] = -1; ans[i][1] = -1; }
    }
    free(pos);
    *returnSize = queriesSize;
    return ans;
}
