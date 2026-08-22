// LeetCode 3711 - Maximum Transactions Without Negative Balance
// https://leetcode.com/problems/maximum-transactions-without-negative-balance/

#include <stdlib.h>
#include <string.h>

/* multiset of ints via sorted dynamic array */
typedef struct { int* a; int n, cap; } Multi;

static void multiAdd(Multi* m, int x) {
    if (m->n == m->cap) { m->cap = m->cap ? m->cap * 2 : 16; m->a = (int*)realloc(m->a, (size_t)m->cap * sizeof(int)); }
    int i = m->n - 1;
    while (i >= 0 && m->a[i] > x) { m->a[i + 1] = m->a[i]; i--; }
    m->a[i + 1] = x;
    m->n++;
}

static void multiRemoveMin(Multi* m) {
    if (m->n == 0) return;
    for (int i = 1; i < m->n; i++) m->a[i - 1] = m->a[i];
    m->n--;
}

int maxTransactions(int* transactions, int transactionsSize) {
    Multi tm = {0};
    int ans = transactionsSize;
    long long s = 0;
    for (int i = 0; i < transactionsSize; i++) {
        int x = transactions[i];
        s += x;
        multiAdd(&tm, x);
        while (s < 0) {
            int y = tm.a[0];
            s -= y;
            ans--;
            multiRemoveMin(&tm);
        }
    }
    free(tm.a);
    return ans;
}
