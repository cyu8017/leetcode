// LeetCode 1387 - Sort Integers by The Power Value
// https://leetcode.com/problems/sort-integers-by-the-power-value/

#include <stdlib.h>

static int power(long long x) {
    int steps = 0;
    while (x != 1) {
        if (x % 2 == 0) x /= 2;
        else x = 3 * x + 1;
        steps++;
    }
    return steps;
}

typedef struct { int val, pow; } Item;
static int cmp_item(const void* a, const void* b) {
    const Item* x = (const Item*)a;
    const Item* y = (const Item*)b;
    if (x->pow != y->pow) return x->pow - y->pow;
    return x->val - y->val;
}

int getKth(int lo, int hi, int k) {
    int n = hi - lo + 1;
    Item* items = (Item*)malloc(n * sizeof(Item));
    for (int i = 0; i < n; i++) {
        items[i].val = lo + i;
        items[i].pow = power(lo + i);
    }
    qsort(items, n, sizeof(Item), cmp_item);
    int ans = items[k - 1].val;
    free(items);
    return ans;
}
