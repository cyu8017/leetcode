// LeetCode 3164 - Find the Number of Good Pairs II
// https://leetcode.com/problems/find-the-number-of-good-pairs-ii/

#include <stdlib.h>

enum { H3164 = 200003 };
typedef struct { int key, val, used; } E3164;

static int* get3164(E3164* ht, int key, int create) {
    unsigned h = ((unsigned)key * 2654435761u) % H3164;
    for (;;) {
        if (!ht[h].used) {
            if (!create) return NULL;
            ht[h].used = 1; ht[h].key = key; ht[h].val = 0;
            return &ht[h].val;
        }
        if (ht[h].key == key) return &ht[h].val;
        h = (h + 1) % H3164;
    }
}

long long numberOfPairs(int* nums1, int nums1Size, int* nums2, int nums2Size, int k) {
    E3164* cnt1 = calloc(H3164, sizeof(E3164));
    int has = 0, mx = 0;
    for (int i = 0; i < nums1Size; i++) {
        if (nums1[i] % k == 0) {
            int x = nums1[i] / k;
            (*get3164(cnt1, x, 1))++;
            has = 1;
            if (x > mx) mx = x;
        }
    }
    if (!has) { free(cnt1); return 0; }
    E3164* cnt2 = calloc(H3164, sizeof(E3164));
    for (int i = 0; i < nums2Size; i++) (*get3164(cnt2, nums2[i], 1))++;
    long long ans = 0;
    for (int i = 0; i < H3164; i++) {
        if (!cnt2[i].used) continue;
        int x = cnt2[i].key, v = cnt2[i].val, s = 0;
        for (int y = x; y <= mx; y += x) {
            int* p = get3164(cnt1, y, 0);
            if (p) s += *p;
        }
        ans += (long long)s * v;
    }
    free(cnt1); free(cnt2);
    return ans;
}
