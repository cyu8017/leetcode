// LeetCode 2462 - Total Cost to Hire K Workers
// https://leetcode.com/problems/total-cost-to-hire-k-workers/

#include <stdlib.h>

typedef struct { int cost, idx; } Item2462;

static void swap2462(Item2462* a, Item2462* b) { Item2462 t = *a; *a = *b; *b = t; }

static int less2462(Item2462 a, Item2462 b) {
    if (a.cost != b.cost) return a.cost < b.cost;
    return a.idx < b.idx;
}

static void push2462(Item2462* h, int* n, Item2462 x) {
    int i = (*n)++;
    h[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (!less2462(h[i], h[p])) break;
        swap2462(&h[i], &h[p]);
        i = p;
    }
}

static Item2462 pop2462(Item2462* h, int* n) {
    Item2462 res = h[0];
    h[0] = h[--(*n)];
    int i = 0;
    for (;;) {
        int l = i * 2 + 1, r = l + 1, best = i;
        if (l < *n && less2462(h[l], h[best])) best = l;
        if (r < *n && less2462(h[r], h[best])) best = r;
        if (best == i) break;
        swap2462(&h[i], &h[best]);
        i = best;
    }
    return res;
}

long long totalCost(int* costs, int costsSize, int k, int candidates) {
    int n = costsSize;
    Item2462* leftH = (Item2462*)malloc((size_t)(candidates + 5) * sizeof(Item2462));
    Item2462* rightH = (Item2462*)malloc((size_t)(candidates + 5) * sizeof(Item2462));
    int ln = 0, rn = 0;
    int l = 0, r = n - 1;
    while (l <= r && ln < candidates) push2462(leftH, &ln, (Item2462){costs[l], l}), l++;
    while (r >= l && rn < candidates) push2462(rightH, &rn, (Item2462){costs[r], r}), r--;
    long long ans = 0;
    for (int t = 0; t < k; t++) {
        int useLeft = 0;
        if (ln > 0 && rn > 0) {
            if (less2462(leftH[0], rightH[0]) || (leftH[0].cost == rightH[0].cost && leftH[0].idx <= rightH[0].idx))
                useLeft = 1;
        } else if (ln > 0) useLeft = 1;
        if (useLeft) {
            Item2462 it = pop2462(leftH, &ln);
            ans += it.cost;
            if (l <= r) push2462(leftH, &ln, (Item2462){costs[l], l}), l++;
        } else {
            Item2462 it = pop2462(rightH, &rn);
            ans += it.cost;
            if (l <= r) push2462(rightH, &rn, (Item2462){costs[r], r}), r--;
        }
    }
    free(leftH); free(rightH);
    return ans;
}
