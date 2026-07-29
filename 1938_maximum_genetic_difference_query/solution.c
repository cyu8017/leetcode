// LeetCode 1938 - Maximum Genetic Difference Query
// https://leetcode.com/problems/maximum-genetic-difference-query/

#include <stdlib.h>

#define BITS 17

typedef struct TrieNode {
    struct TrieNode* child[2];
    int cnt;
} TrieNode;

static TrieNode* trieNew(void) {
    return (TrieNode*)calloc(1, sizeof(TrieNode));
}

static void trieFree(TrieNode* node) {
    if (!node) return;
    trieFree(node->child[0]);
    trieFree(node->child[1]);
    free(node);
}

static void trieUpdate(TrieNode* root, int num, int delta) {
    TrieNode* node = root;
    for (int b = BITS; b >= 0; b--) {
        int bit = (num >> b) & 1;
        if (!node->child[bit]) node->child[bit] = trieNew();
        node = node->child[bit];
        node->cnt += delta;
    }
}

static int trieMaxXor(TrieNode* root, int num) {
    TrieNode* node = root;
    int res = 0;
    for (int b = BITS; b >= 0; b--) {
        int bit = (num >> b) & 1;
        int want = 1 - bit;
        if (node->child[want] && node->child[want]->cnt > 0) {
            res |= 1 << b;
            node = node->child[want];
        } else {
            node = node->child[bit];
        }
    }
    return res;
}

typedef struct { int qi; int val; } QItem;

static void dfs(int u, int** children, int* childSize, QItem** qmap, int* qmapSize, TrieNode* root, int* ans) {
    trieUpdate(root, u, 1);
    for (int i = 0; i < qmapSize[u]; i++) {
        ans[qmap[u][i].qi] = trieMaxXor(root, qmap[u][i].val);
    }
    for (int i = 0; i < childSize[u]; i++) {
        dfs(children[u][i], children, childSize, qmap, qmapSize, root, ans);
    }
    trieUpdate(root, u, -1);
}

int* maxGeneticDifference(int* parents, int parentsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int n = parentsSize;
    int** children = (int**)calloc((size_t)n, sizeof(int*));
    int* childSize = (int*)calloc((size_t)n, sizeof(int));
    int* childCap = (int*)calloc((size_t)n, sizeof(int));
    int root = 0;
    for (int i = 0; i < n; i++) {
        if (parents[i] == -1) { root = i; continue; }
        int p = parents[i];
        if (childSize[p] == childCap[p]) {
            childCap[p] = childCap[p] ? childCap[p] * 2 : 4;
            children[p] = (int*)realloc(children[p], (size_t)childCap[p] * sizeof(int));
        }
        children[p][childSize[p]++] = i;
    }
    QItem** qmap = (QItem**)calloc((size_t)n, sizeof(QItem*));
    int* qmapSize = (int*)calloc((size_t)n, sizeof(int));
    int* qmapCap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        int node = queries[i][0], val = queries[i][1];
        if (qmapSize[node] == qmapCap[node]) {
            qmapCap[node] = qmapCap[node] ? qmapCap[node] * 2 : 4;
            qmap[node] = (QItem*)realloc(qmap[node], (size_t)qmapCap[node] * sizeof(QItem));
        }
        qmap[node][qmapSize[node]++] = (QItem){i, val};
    }
    int* ans = (int*)calloc((size_t)queriesSize, sizeof(int));
    TrieNode* trie = trieNew();
    dfs(root, children, childSize, qmap, qmapSize, trie, ans);
    trieFree(trie);
    for (int i = 0; i < n; i++) { free(children[i]); free(qmap[i]); }
    free(children); free(childSize); free(childCap);
    free(qmap); free(qmapSize); free(qmapCap);
    *returnSize = queriesSize;
    return ans;
}
