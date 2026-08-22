// LeetCode 3811 - Number Of Alternating Xor Partitions
// https://leetcode.com/problems/number-of-alternating-xor-partitions/

#include <stdlib.h>

typedef struct { int key; int val; int used; } Map3811;

static int map_get(Map3811* m, int cap, int key) {
    unsigned h = (unsigned)key * 2654435761u;
    int i = (int)(h % (unsigned)cap);
    for (int t = 0; t < cap; t++) {
        int j = (i + t) % cap;
        if (!m[j].used) return 0;
        if (m[j].key == key) return m[j].val;
    }
    return 0;
}
static void map_add(Map3811* m, int cap, int key, int delta, int mod) {
    unsigned h = (unsigned)key * 2654435761u;
    int i = (int)(h % (unsigned)cap);
    for (int t = 0; t < cap; t++) {
        int j = (i + t) % cap;
        if (!m[j].used) { m[j].used = 1; m[j].key = key; m[j].val = delta % mod; return; }
        if (m[j].key == key) { m[j].val = (m[j].val + delta) % mod; return; }
    }
}

int alternatingXOR(int* nums, int numsSize, int target1, int target2) {
    const int mod = 1000000007;
    int cap = 1;
    while (cap < numsSize * 4 + 16) cap <<= 1;
    Map3811* cnt1 = (Map3811*)calloc((size_t)cap, sizeof(Map3811));
    Map3811* cnt2 = (Map3811*)calloc((size_t)cap, sizeof(Map3811));
    map_add(cnt2, cap, 0, 1, mod);
    int pre = 0, ans = 0;
    for (int i = 0; i < numsSize; i++) {
        pre ^= nums[i];
        int a = map_get(cnt2, cap, pre ^ target1);
        int b = map_get(cnt1, cap, pre ^ target2);
        ans = (a + b) % mod;
        map_add(cnt1, cap, pre, a, mod);
        map_add(cnt2, cap, pre, b, mod);
    }
    free(cnt1); free(cnt2);
    return ans;
}
