// LeetCode 1516 - Move Sub-Tree of N-Ary Tree
// https://leetcode.com/problems/move-sub-tree-of-n-ary-tree/

#include <stdlib.h>

struct Node {
    int val;
    int numChildren;
    struct Node** children;
};

static struct Node* findParent(struct Node* node, struct Node* target) {
    for (int i = 0; i < node->numChildren; i++) {
        if (node->children[i] == target) return node;
        struct Node* found = findParent(node->children[i], target);
        if (found) return found;
    }
    return NULL;
}

static int isAncestor(struct Node* a, struct Node* b, struct Node* root) {
    struct Node* cur = b;
    while (cur && cur != root) {
        struct Node* p = findParent(root, cur);
        if (!p) return 0;
        if (p == a) return 1;
        cur = p;
    }
    return 0;
}

static void removeChild(struct Node* parent, struct Node* child) {
    int idx = -1;
    for (int i = 0; i < parent->numChildren; i++) {
        if (parent->children[i] == child) { idx = i; break; }
    }
    if (idx < 0) return;
    for (int i = idx; i + 1 < parent->numChildren; i++) parent->children[i] = parent->children[i + 1];
    parent->numChildren--;
}

static void replaceChild(struct Node* parent, struct Node* oldChild, struct Node* newChild) {
    for (int i = 0; i < parent->numChildren; i++) {
        if (parent->children[i] == oldChild) {
            parent->children[i] = newChild;
            return;
        }
    }
}

static void appendChild(struct Node* parent, struct Node* child) {
    parent->children = (struct Node**)realloc(parent->children, (size_t)(parent->numChildren + 1) * sizeof(struct Node*));
    parent->children[parent->numChildren++] = child;
}

struct Node* moveSubTree(struct Node* root, struct Node* p, struct Node* q) {
    struct Node* p_parent = (p == root) ? NULL : findParent(root, p);
    if (p_parent == q) return root;

    if (isAncestor(p, q, root)) {
        struct Node* q_parent = findParent(root, q);
        removeChild(q_parent, q);
        if (!p_parent) root = q;
        else replaceChild(p_parent, p, q);
        appendChild(q, p);
    } else {
        if (!p_parent) root = q;
        else removeChild(p_parent, p);
        appendChild(q, p);
    }
    return root;
}
