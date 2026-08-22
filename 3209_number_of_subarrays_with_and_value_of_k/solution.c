// LeetCode 3209 - Number of Subarrays With AND Value of K
// https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/

#include <stdlib.h>
#include <string.h>

enum { H3209 = 4099 };
typedef struct { int key, val, used; } E3209;

static void htclear(E3209* ht) { memset(ht, 0, H3209 * sizeof(E3209)); }
static int* htget(E3209* ht, int key, int create) {
    unsigned h = ((unsigned)key * 2654435761u) % H3209;
    for (;;) {
        if (!ht[h].used) {
            if (!create) return NULL;
            ht[h].used = 1; ht[h].key = key; ht[h].val = 0;
            return &ht[h].val;
        }
        if (ht[h].key == key) return &ht[h].val;
        h = (h + 1) % H3209;
    }
}

long long countSubarrays(int* nums, int numsSize, int k) {
    E3209 pre[H3209], cur[H3209];
    htclear(pre);
    long long ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        htclear(cur);
        for (int t = 0; t < H3209; t++) if (pre[t].used)
            *htget(cur, x & pre[t].key, 1) += pre[t].val;
        (*htget(cur, x, 1))++;
        int* pk = htget(cur, k, 0);
        if (pk) ans += *pk;
        memcpy(pre, cur, sizeof(pre));
    }
    return ans;
}
