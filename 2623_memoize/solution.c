// LeetCode 2623 - Memoize
// https://leetcode.com/problems/memoize/

#include <stdlib.h>
#include <stdbool.h>

typedef int (*IntFn)(int);

typedef struct {
    int key;
    int val;
    bool set;
} Entry;

typedef struct {
    IntFn fn;
    Entry* cache;
    int cap;
} Memo;

static int* memo_lookup(Memo* m, int x, bool* found) {
    unsigned h = (unsigned)x & (m->cap - 1);
    while (m->cache[h].set) {
        if (m->cache[h].key == x) { *found = true; return &m->cache[h].val; }
        h = (h + 1) & (m->cap - 1);
    }
    *found = false;
    return NULL;
}

Memo* memoizeCreate(IntFn fn) {
    Memo* m = (Memo*)malloc(sizeof(Memo));
    m->fn = fn;
    m->cap = 1 << 12;
    m->cache = (Entry*)calloc((size_t)m->cap, sizeof(Entry));
    return m;
}

int memoizeCall(Memo* m, int x) {
    bool found = false;
    unsigned h = (unsigned)x & (m->cap - 1);
    while (m->cache[h].set) {
        if (m->cache[h].key == x) return m->cache[h].val;
        h = (h + 1) & (m->cap - 1);
    }
    int v = m->fn(x);
    m->cache[h].set = true;
    m->cache[h].key = x;
    m->cache[h].val = v;
    return v;
}

void memoizeFree(Memo* m) {
    free(m->cache);
    free(m);
}
