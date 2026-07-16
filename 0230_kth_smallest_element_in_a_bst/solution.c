// LeetCode 0230 - Kth Smallest Element in a BST
// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int kthSmallest(struct TreeNode* root, int k) {
    struct TreeNode** stack = malloc((size_t)k * sizeof(struct TreeNode*));
    int stackSize = 0;
    struct TreeNode* current = root;

    while (current || stackSize > 0) {
        while (current) {
            stack = realloc(stack, (size_t)(stackSize + 1) * sizeof(struct TreeNode*));
            stack[stackSize++] = current;
            current = current->left;
        }
        current = stack[--stackSize];
        k--;
        if (k == 0) {
            int value = current->val;
            free(stack);
            return value;
        }
        current = current->right;
    }

    free(stack);
    return -1;
}
