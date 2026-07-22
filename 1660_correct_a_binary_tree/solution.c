// LeetCode 1660 - Correct a Binary Tree
// https://leetcode.com/problems/correct-a-binary-tree/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct {
    struct TreeNode** data;
    int size;
    int cap;
} NodeSet;

static void setInit(NodeSet* s) {
    s->cap = 64;
    s->size = 0;
    s->data = (struct TreeNode**)malloc((size_t)s->cap * sizeof(struct TreeNode*));
}

static int setHas(NodeSet* s, struct TreeNode* n) {
    for (int i = 0; i < s->size; i++) if (s->data[i] == n) return 1;
    return 0;
}

static void setAdd(NodeSet* s, struct TreeNode* n) {
    if (s->size == s->cap) {
        s->cap *= 2;
        s->data = (struct TreeNode**)realloc(s->data, (size_t)s->cap * sizeof(struct TreeNode*));
    }
    s->data[s->size++] = n;
}

static struct TreeNode* dfs(struct TreeNode* node, NodeSet* seen) {
    if (!node) return NULL;
    if (node->right && setHas(seen, node->right)) return NULL;
    setAdd(seen, node);
    node->right = dfs(node->right, seen);
    node->left = dfs(node->left, seen);
    return node;
}

struct TreeNode* correctBinaryTree(struct TreeNode* root) {
    NodeSet seen;
    setInit(&seen);
    struct TreeNode* ans = dfs(root, &seen);
    free(seen.data);
    return ans;
}
