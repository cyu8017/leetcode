// LeetCode 3897 - Maximum Value Of Concatenated Binary Segments
// https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/

#include <stdlib.h>

enum { MOD3897 = 1000000007 };

typedef struct { int x, y; } Pair3897;

static int group3897(Pair3897 p) {
    if (p.y == 0) return 0;
    if (p.x > 0) return 1;
    return 2;
}

static int cmp3897(const void* aa, const void* bb) {
    Pair3897 a = *(const Pair3897*)aa, b = *(const Pair3897*)bb;
    int g1 = group3897(a), g2 = group3897(b);
    if (g1 != g2) return g1 - g2;
    if (g1 == 0) return b.x - a.x;
    if (g1 == 1) {
        if (a.x != b.x) return b.x - a.x;
        return a.y - b.y;
    }
    return a.y - b.y;
}

int maxValue(int* nums1, int nums1Size, int* nums0, int nums0Size) {
    (void)nums0Size;
    int n = nums1Size;
    Pair3897* pairs = malloc((size_t)n * sizeof(Pair3897));
    int b = 0;
    for (int i = 0; i < n; i++) {
        pairs[i].x = nums1[i];
        pairs[i].y = nums0[i];
        b += nums1[i] + nums0[i];
    }
    qsort(pairs, (size_t)n, sizeof(Pair3897), cmp3897);
    int* p = malloc((size_t)b * sizeof(int));
    p[0] = 1;
    for (int i = 1; i < b; i++) p[i] = (int)((long long)p[i - 1] * 2 % MOD3897);
    int ans = 0;
    b--;
    for (int i = 0; i < n; i++) {
        int cnt1 = pairs[i].x, cnt0 = pairs[i].y;
        while (cnt1 > 0) {
            ans = (ans + p[b]) % MOD3897;
            b--;
            cnt1--;
        }
        b -= cnt0;
    }
    free(pairs); free(p);
    return ans;
}
