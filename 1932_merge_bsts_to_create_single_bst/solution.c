// LeetCode 1932 - Merge BSTs to Create Single BST
// https://leetcode.com/problems/merge-bsts-to-create-single-bst/

#include <stdlib.h>
#include <limits.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct { int key; struct TreeNode* node; } MapEntry;
typedef struct { int key; int cnt; } CountEntry;

static int findMap(MapEntry* m, int n, int key) {
    for (int i = 0; i < n; i++) if (m[i].key == key) return i;
    return -1;
}

static int findCnt(CountEntry* c, int n, int key) {
    for (int i = 0; i < n; i++) if (c[i].key == key) return i;
    return -1;
}

static void addCnt(CountEntry* c, int* n, int key) {
    int i = findCnt(c, *n, key);
    if (i < 0) { c[*n].key = key; c[*n].cnt = 1; (*n)++; }
    else c[i].cnt++;
}

static int merge(struct TreeNode* node, MapEntry* map, int* mapN) {
    if (!node) return 1;
    if (node->left) {
        int i = findMap(map, *mapN, node->left->val);
        if (i >= 0) {
            node->left = map[i].node;
            map[i] = map[--(*mapN)];
        }
    }
    if (node->right) {
        int i = findMap(map, *mapN, node->right->val);
        if (i >= 0) {
            node->right = map[i].node;
            map[i] = map[--(*mapN)];
        }
    }
    return merge(node->left, map, mapN) && merge(node->right, map, mapN);
}

static int isValid(struct TreeNode* node, long long lo, long long hi) {
    if (!node) return 1;
    if (!(lo < node->val && node->val < hi)) return 0;
    return isValid(node->left, lo, node->val) && isValid(node->right, node->val, hi);
}

struct TreeNode* canMerge(struct TreeNode** trees, int treesSize) {
    MapEntry* map = (MapEntry*)malloc((size_t)treesSize * sizeof(MapEntry));
    CountEntry* count = (CountEntry*)malloc((size_t)treesSize * 3 * sizeof(CountEntry));
    int mapN = 0, cntN = 0;
    for (int i = 0; i < treesSize; i++) {
        struct TreeNode* t = trees[i];
        map[mapN].key = t->val;
        map[mapN].node = t;
        mapN++;
        addCnt(count, &cntN, t->val);
        if (t->left) addCnt(count, &cntN, t->left->val);
        if (t->right) addCnt(count, &cntN, t->right->val);
    }
    struct TreeNode* root = NULL;
    int rootCount = 0;
    for (int i = 0; i < treesSize; i++) {
        int ci = findCnt(count, cntN, trees[i]->val);
        if (count[ci].cnt == 1) {
            root = trees[i];
            rootCount++;
        }
    }
    if (rootCount != 1) {
        free(map); free(count);
        return NULL;
    }
    int ri = findMap(map, mapN, root->val);
    map[ri] = map[--mapN];
    if (!merge(root, map, &mapN) || mapN != 0) {
        free(map); free(count);
        return NULL;
    }
    free(map); free(count);
    return isValid(root, LLONG_MIN, LLONG_MAX) ? root : NULL;
}
