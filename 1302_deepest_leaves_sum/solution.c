// LeetCode 1302 - Deepest Leaves Sum
// https://leetcode.com/problems/deepest-leaves-sum/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int deepestLeavesSum(struct TreeNode* root) {
    if (!root) return 0;
    struct TreeNode** level = (struct TreeNode**)malloc(sizeof(struct TreeNode*));
    int levelSize = 1;
    level[0] = root;
    int answer = 0;
    while (levelSize > 0) {
        answer = 0;
        struct TreeNode** next = (struct TreeNode**)malloc(levelSize * 2 * sizeof(struct TreeNode*));
        int nextSize = 0;
        for (int i = 0; i < levelSize; i++) {
            answer += level[i]->val;
            if (level[i]->left) next[nextSize++] = level[i]->left;
            if (level[i]->right) next[nextSize++] = level[i]->right;
        }
        free(level);
        level = next;
        levelSize = nextSize;
    }
    free(level);
    return answer;
}
