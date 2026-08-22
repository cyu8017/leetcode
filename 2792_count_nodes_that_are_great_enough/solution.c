// LeetCode 2792 - Count Nodes That Are Great Enough
// https://leetcode.com/problems/count-nodes-that-are-great-enough/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

typedef struct { int* a; int n; int* ans; int k; } Acc;

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

static int* dfs(struct TreeNode* node, int* outn, Acc* acc) {
    if (!node) { *outn = 0; return NULL; }
    int ln = 0, rn = 0;
    int* L = dfs(node->left, &ln, acc);
    int* R = dfs(node->right, &rn, acc);
    int n = 1 + ln + rn;
    int* vals = (int*)malloc(n * sizeof(int));
    vals[0] = node->val;
    for (int i = 0; i < ln; i++) vals[1 + i] = L[i];
    for (int i = 0; i < rn; i++) vals[1 + ln + i] = R[i];
    free(L); free(R);
    int smaller = 0;
    for (int i = 0; i < n; i++) if (vals[i] < node->val) smaller++;
    if (smaller >= acc->k) (*acc->ans)++;
    *outn = n;
    return vals;
}

int countGreatEnoughNodes(struct TreeNode* root, int k) {
    int ans = 0;
    Acc acc = {0, 0, &ans, k};
    int n = 0;
    free(dfs(root, &n, &acc));
    return ans;
}
