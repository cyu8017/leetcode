// LeetCode 0337 - House Robber III
// https://leetcode.com/problems/house-robber-iii/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

typedef struct {
    int withRob;
    int withoutRob;
} RobResult;

static RobResult dfs(struct TreeNode* node) {
    if (node == NULL) {
        RobResult empty = {0, 0};
        return empty;
    }

    RobResult left = dfs(node->left);
    RobResult right = dfs(node->right);

    RobResult result;
    result.withRob = node->val + left.withoutRob + right.withoutRob;
    int leftBest = left.withRob > left.withoutRob ? left.withRob : left.withoutRob;
    int rightBest = right.withRob > right.withoutRob ? right.withRob : right.withoutRob;
    result.withoutRob = leftBest + rightBest;
    return result;
}

int rob(struct TreeNode* root) {
    RobResult result = dfs(root);
    return result.withRob > result.withoutRob ? result.withRob : result.withoutRob;
}
