// LeetCode 2479 - Maximum XOR of Two Non-Overlapping Subtrees
// https://leetcode.com/problems/maximum-xor-of-two-non-overlapping-subtrees/

#include <stdlib.h>
#include <string.h>

typedef struct Trie2479 {
    struct Trie2479* child[2];
} Trie2479;

static int** g2479;
static int* deg2479;
static int* cap2479;
static long long* sum2479;
static int* values2479;
static long long ans2479;
static Trie2479* root2479;

static void add2479(int a, int b) {
    if (deg2479[a] == cap2479[a]) {
        cap2479[a] = cap2479[a] ? cap2479[a] * 2 : 4;
        g2479[a] = (int*)realloc(g2479[a], (size_t)cap2479[a] * sizeof(int));
    }
    g2479[a][deg2479[a]++] = b;
}

static long long dfsSum2479(int u, int p) {
    long long s = values2479[u];
    for (int i = 0; i < deg2479[u]; i++) {
        int v = g2479[u][i];
        if (v != p) s += dfsSum2479(v, u);
    }
    sum2479[u] = s;
    return s;
}

static void insert2479(long long x) {
    Trie2479* cur = root2479;
    for (int b = 46; b >= 0; b--) {
        int bit = (int)((x >> b) & 1);
        if (!cur->child[bit]) cur->child[bit] = (Trie2479*)calloc(1, sizeof(Trie2479));
        cur = cur->child[bit];
    }
}

static long long query2479(long long x) {
    Trie2479* cur = root2479;
    if (!cur->child[0] && !cur->child[1]) return 0;
    long long ans = 0;
    for (int b = 46; b >= 0; b--) {
        int bit = (int)((x >> b) & 1);
        int want = bit ^ 1;
        if (cur->child[want]) {
            ans |= 1LL << b;
            cur = cur->child[want];
        } else if (cur->child[bit]) {
            cur = cur->child[bit];
        } else return ans;
    }
    return ans;
}

static void freeTrie2479(Trie2479* node) {
    if (!node) return;
    freeTrie2479(node->child[0]);
    freeTrie2479(node->child[1]);
    free(node);
}

static void dfs2479(int u, int p) {
    for (int i = 0; i < deg2479[u]; i++) {
        int v = g2479[u][i];
        if (v == p) continue;
        long long xorv = query2479(sum2479[v]);
        if (xorv > ans2479) ans2479 = xorv;
        dfs2479(v, u);
        insert2479(sum2479[v]);
    }
}

long long maxXor(int n, int** edges, int edgesSize, int* edgesColSize, int* values, int valuesSize) {
    (void)edgesColSize; (void)valuesSize;
    g2479 = (int**)calloc((size_t)n, sizeof(int*));
    deg2479 = (int*)calloc((size_t)n, sizeof(int));
    cap2479 = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        add2479(edges[i][0], edges[i][1]);
        add2479(edges[i][1], edges[i][0]);
    }
    sum2479 = (long long*)malloc((size_t)n * sizeof(long long));
    values2479 = values;
    dfsSum2479(0, -1);
    root2479 = (Trie2479*)calloc(1, sizeof(Trie2479));
    ans2479 = 0;
    dfs2479(0, -1);
    long long result = ans2479;
    freeTrie2479(root2479);
    for (int i = 0; i < n; i++) free(g2479[i]);
    free(g2479); free(deg2479); free(cap2479); free(sum2479);
    return result;
}
