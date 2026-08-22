// LeetCode 2196 - Create Binary Tree From Descriptions
// https://leetcode.com/problems/create-binary-tree-from-descriptions/

#include <stdlib.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

typedef struct { int key; struct TreeNode* node; bool used; } NodeMap;
typedef struct { int key; bool used; } BoolMap;

static unsigned hush(int x) { return (unsigned)x * 2654435761u; }

static NodeMap* getNode(NodeMap* t, int cap, int key) {
    unsigned h = hush(key) % (unsigned)cap;
    for (int i = 0; i < cap; i++) {
        unsigned idx = (h + i) % (unsigned)cap;
        if (!t[idx].used) {
            t[idx].used = true; t[idx].key = key;
            t[idx].node = (struct TreeNode*)calloc(1, sizeof(struct TreeNode));
            t[idx].node->val = key;
            return &t[idx];
        }
        if (t[idx].key == key) return &t[idx];
    }
    return NULL;
}

static void setChild(BoolMap* t, int cap, int key) {
    unsigned h = hush(key) % (unsigned)cap;
    for (int i = 0; i < cap; i++) {
        unsigned idx = (h + i) % (unsigned)cap;
        if (!t[idx].used) { t[idx].used = true; t[idx].key = key; return; }
        if (t[idx].key == key) return;
    }
}

static bool isChild(BoolMap* t, int cap, int key) {
    unsigned h = hush(key) % (unsigned)cap;
    for (int i = 0; i < cap; i++) {
        unsigned idx = (h + i) % (unsigned)cap;
        if (!t[idx].used) return false;
        if (t[idx].key == key) return true;
    }
    return false;
}

struct TreeNode* createBinaryTree(int** descriptions, int descriptionsSize, int* descriptionsColSize) {
    (void)descriptionsColSize;
    int cap = 1 << 14;
    NodeMap* nodes = (NodeMap*)calloc((size_t)cap, sizeof(NodeMap));
    BoolMap* child = (BoolMap*)calloc((size_t)cap, sizeof(BoolMap));
    for (int i = 0; i < descriptionsSize; i++) {
        int p = descriptions[i][0], c = descriptions[i][1], isLeft = descriptions[i][2];
        NodeMap* pn = getNode(nodes, cap, p);
        NodeMap* cn = getNode(nodes, cap, c);
        if (isLeft == 1) pn->node->left = cn->node;
        else pn->node->right = cn->node;
        setChild(child, cap, c);
    }
    struct TreeNode* root = NULL;
    for (int i = 0; i < cap; i++) {
        if (nodes[i].used && !isChild(child, cap, nodes[i].key)) {
            root = nodes[i].node;
            break;
        }
    }
    free(nodes); free(child);
    return root;
}
