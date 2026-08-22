// LeetCode 2791 - Count Paths That Can Form a Palindrome in a Tree
// https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/

#include <stdlib.h>

typedef struct { int key, cnt, used; } E;
typedef struct Ctx {
    int** g; int* gsz;
    char* s;
    E* ht; int htsz;
    long long ans;
} Ctx;

static void ht_add(Ctx* c, int mask, int delta) {
    unsigned h = (unsigned)mask % c->htsz;
    while (c->ht[h].used && c->ht[h].key != mask) h = (h + 1) % c->htsz;
    if (!c->ht[h].used) { c->ht[h].used = 1; c->ht[h].key = mask; c->ht[h].cnt = 0; }
    c->ht[h].cnt += delta;
}
static int ht_get(Ctx* c, int mask) {
    unsigned h = (unsigned)mask % c->htsz;
    while (c->ht[h].used && c->ht[h].key != mask) h = (h + 1) % c->htsz;
    return c->ht[h].used ? c->ht[h].cnt : 0;
}

static void dfs(Ctx* c, int u, int mask) {
    for (int i = 0; i < c->gsz[u]; i++) {
        int v = c->g[u][i];
        int nm = mask ^ (1 << (c->s[v] - 'a'));
        c->ans += ht_get(c, nm);
        for (int b = 0; b < 26; b++) c->ans += ht_get(c, nm ^ (1 << b));
        ht_add(c, nm, 1);
        dfs(c, v, nm);
    }
}

long long countPalindromePaths(int* parent, int parentSize, char* s) {
    int n = parentSize;
    int* gsz = (int*)calloc(n, sizeof(int));
    for (int i = 1; i < n; i++) gsz[parent[i]]++;
    int** g = (int**)malloc(n * sizeof(int*));
    int* fill = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < n; i++) g[i] = (int*)malloc(gsz[i] * sizeof(int));
    for (int i = 1; i < n; i++) g[parent[i]][fill[parent[i]]++] = i;
    Ctx c;
    c.g = g; c.gsz = gsz; c.s = s; c.ans = 0;
    c.htsz = 1; while (c.htsz < n * 4 + 16) c.htsz <<= 1;
    c.ht = (E*)calloc(c.htsz, sizeof(E));
    ht_add(&c, 0, 1);
    dfs(&c, 0, 0);
    long long ans = c.ans;
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gsz); free(fill); free(c.ht);
    return ans;
}
