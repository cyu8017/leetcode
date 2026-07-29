// LeetCode 0559 - Maximum Depth of N-ary Tree
// https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

#include <stddef.h>

struct Node {
    int val;
    int numChildren;
    struct Node** children;
};

int maxDepth(struct Node* root) {
    if (root == NULL) {
        return 0;
    }
    if (root->numChildren == 0) {
        return 1;
    }
    int best = 0;
    for (int i = 0; i < root->numChildren; i++) {
        int depth = maxDepth(root->children[i]);
        if (depth > best) {
            best = depth;
        }
    }
    return best + 1;
}
