// LeetCode 0987 - Vertical Order Traversal of a Binary Tree
// https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct { int col, row, val; } Item;
static int cmpItem(const void* a, const void* b) {
    const Item* x = a; const Item* y = b;
    if (x->col != y->col) return x->col - y->col;
    if (x->row != y->row) return x->row - y->row;
    return x->val - y->val;
}

static Item* items;
static int in, icap;

static void dfs(struct TreeNode* node, int row, int col) {
    if (!node) return;
    if (in == icap) { icap *= 2; items = realloc(items, (size_t)icap * sizeof(Item)); }
    items[in].col = col; items[in].row = row; items[in].val = node->val; in++;
    dfs(node->left, row + 1, col - 1);
    dfs(node->right, row + 1, col + 1);
}

int** verticalTraversal(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
    icap = 64; in = 0;
    items = (Item*)malloc((size_t)icap * sizeof(Item));
    dfs(root, 0, 0);
    qsort(items, (size_t)in, sizeof(Item), cmpItem);
    int** ans = (int**)malloc((size_t)in * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)in * sizeof(int));
    int groups = 0, i = 0;
    while (i < in) {
        int col = items[i].col, j = i;
        while (j < in && items[j].col == col) j++;
        int len = j - i;
        ans[groups] = (int*)malloc((size_t)len * sizeof(int));
        for (int k = 0; k < len; k++) ans[groups][k] = items[i + k].val;
        (*returnColumnSizes)[groups] = len;
        groups++;
        i = j;
    }
    free(items);
    *returnSize = groups;
    return ans;
}
