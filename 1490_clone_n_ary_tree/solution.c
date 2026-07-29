// LeetCode 1490 - Clone N-ary Tree
// https://leetcode.com/problems/clone-n-ary-tree/

#include <stdlib.h>

struct Node {
    int val;
    int numChildren;
    struct Node** children;
};

struct Node* cloneTree(struct Node* root) {
    if (!root) return NULL;
    struct Node* neu = (struct Node*)malloc(sizeof(struct Node));
    neu->val = root->val;
    neu->numChildren = root->numChildren;
    neu->children = NULL;
    if (root->numChildren) {
        neu->children = (struct Node**)malloc(root->numChildren * sizeof(struct Node*));
        for (int i = 0; i < root->numChildren; i++)
            neu->children[i] = cloneTree(root->children[i]);
    }
    return neu;
}
