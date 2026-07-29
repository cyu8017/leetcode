// LeetCode 0898 - Bitwise ORs of Subarrays
// https://leetcode.com/problems/bitwise-ors-of-subarrays/

#include <stdlib.h>
#include <stdbool.h>

int subarrayBitwiseORs(int* arr, int arrSize) {
    // use hash set for ans and cur
    int scap = 1 << 18;
    int* slots = (int*)malloc((size_t)scap * sizeof(int));
    bool* used = (bool*)calloc((size_t)scap, sizeof(bool));
    int ansCount = 0;

    #define H(x) (((unsigned)(x) * 2654435761u) & (unsigned)(scap - 1))
    #define ADD_SET(x, added) do { \
        unsigned h = H(x); \
        while (used[h]) { if (slots[h] == (x)) { added = 0; break; } h = (h + 1) & (scap - 1); } \
        if (!used[h]) { used[h] = true; slots[h] = (x); added = 1; } \
    } while (0)

    int cur[64], ncur = 0;
    int nxt[64];
    for (int i = 0; i < arrSize; i++) {
        int x = arr[i];
        int nn = 0;
        nxt[nn++] = x;
        for (int j = 0; j < ncur; j++) {
            int v = cur[j] | x;
            bool dup = false;
            for (int t = 0; t < nn; t++) if (nxt[t] == v) { dup = true; break; }
            if (!dup) nxt[nn++] = v;
        }
        ncur = nn;
        for (int j = 0; j < nn; j++) cur[j] = nxt[j];
        for (int j = 0; j < ncur; j++) {
            int added = 0;
            ADD_SET(cur[j], added);
            if (added) ansCount++;
        }
    }
    free(slots); free(used);
    return ansCount;
#undef H
#undef ADD_SET
}
