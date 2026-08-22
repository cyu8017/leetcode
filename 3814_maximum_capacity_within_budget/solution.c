// LeetCode 3814 - Maximum Capacity Within Budget
// https://leetcode.com/problems/maximum-capacity-within-budget/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { int a, b; } Pair3814;
typedef struct { int b, i; } Node3814;

static int cmp_pair(const void* x, const void* y) {
    const Pair3814* a = x, *b = y;
    if (a->a != b->a) return a->a - b->a;
    return a->b - b->b;
}

static void push3814(Node3814* h, int* n, Node3814 x) {
    int i = (*n)++;
    h[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p].b > h[i].b || (h[p].b == h[i].b && h[p].i > h[i].i)) break;
        Node3814 t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}
static Node3814 pop3814(Node3814* h, int* n) {
    Node3814 r = h[0];
    h[0] = h[--(*n)];
    int i = 0;
    for (;;) {
        int l = 2*i+1, rgt = 2*i+2, s = i;
        if (l < *n && (h[l].b > h[s].b || (h[l].b == h[s].b && h[l].i > h[s].i))) s = l;
        if (rgt < *n && (h[rgt].b > h[s].b || (h[rgt].b == h[s].b && h[rgt].i > h[s].i))) s = rgt;
        if (s == i) break;
        Node3814 t = h[i]; h[i] = h[s]; h[s] = t;
        i = s;
    }
    return r;
}

int maxCapacity(int* costs, int costsSize, int* capacity, int capacitySize, int budget) {
    (void)capacitySize;
    Pair3814* arr = (Pair3814*)malloc((size_t)costsSize * sizeof(Pair3814));
    int asz = 0;
    for (int k = 0; k < costsSize; k++) {
        if (costs[k] < budget) arr[asz++] = (Pair3814){costs[k], capacity[k]};
    }
    if (asz == 0) { free(arr); return 0; }
    qsort(arr, (size_t)asz, sizeof(Pair3814), cmp_pair);
    bool* alive = (bool*)malloc((size_t)asz * sizeof(bool));
    Node3814* h = (Node3814*)malloc((size_t)asz * sizeof(Node3814));
    int hsz = 0;
    for (int i = 0; i < asz; i++) { alive[i] = true; push3814(h, &hsz, (Node3814){arr[i].b, i}); }
    while (hsz > 0 && !alive[h[0].i]) pop3814(h, &hsz);
    int ans = h[0].b;
    int i = 0, j = asz - 1;
    while (i < j) {
        alive[i] = false;
        while (i < j && arr[i].a + arr[j].a >= budget) { alive[j] = false; j--; }
        while (hsz > 0 && !alive[h[0].i]) pop3814(h, &hsz);
        if (hsz > 0) {
            int cand = arr[i].b + h[0].b;
            if (cand > ans) ans = cand;
        }
        i++;
    }
    free(arr); free(alive); free(h);
    return ans;
}
