// LeetCode 3319 - K-th Largest Perfect Subtree Size in Binary Tree
// https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

#include <stdlib.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct { int h, sz; bool perf; } Info;

static int* sizes;
static int sn, scap;

static int cmpDesc(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (y > x) - (y < x);
}

static Info dfs3319(struct TreeNode* node) {
    if (!node) return (Info){0, 0, true};
    Info L = dfs3319(node->left);
    Info R = dfs3319(node->right);
    int sz = L.sz + R.sz + 1;
    bool perf = L.perf && R.perf && L.h == R.h;
    if (perf) {
        if (sn == scap) { scap = scap ? scap * 2 : 16; sizes = realloc(sizes, (size_t)scap * sizeof(int)); }
        sizes[sn++] = sz;
    }
    int h = L.h > R.h ? L.h : R.h;
    return (Info){h + 1, sz, perf};
}

int kthLargestPerfectSubtree(struct TreeNode* root, int k) {
    sizes = NULL; sn = 0; scap = 0;
    dfs3319(root);
    qsort(sizes, (size_t)sn, sizeof(int), cmpDesc);
    int ans = (k > sn) ? -1 : sizes[k - 1];
    free(sizes);
    return ans;
}
