// LeetCode 0549 - Binary Tree Longest Consecutive Sequence II
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

typedef struct {
    int inc;
    int dec;
} SequenceLengths;

static int maxInt(int left, int right) {
    return left > right ? left : right;
}

static SequenceLengths dfs(struct TreeNode* node, int* best) {
    if (!node) {
        SequenceLengths empty = {0, 0};
        return empty;
    }

    const SequenceLengths leftLengths = dfs(node->left, best);
    const SequenceLengths rightLengths = dfs(node->right, best);

    int inc = 1;
    int dec = 1;
    if (node->left) {
        if (node->left->val == node->val + 1) {
            inc = maxInt(inc, leftLengths.inc + 1);
        } else if (node->left->val == node->val - 1) {
            dec = maxInt(dec, leftLengths.dec + 1);
        }
    }
    if (node->right) {
        if (node->right->val == node->val + 1) {
            inc = maxInt(inc, rightLengths.inc + 1);
        } else if (node->right->val == node->val - 1) {
            dec = maxInt(dec, rightLengths.dec + 1);
        }
    }

    if (node->left && node->right) {
        if (node->left->val + 1 == node->val && node->val + 1 == node->right->val) {
            *best = maxInt(*best, leftLengths.dec + 1 + rightLengths.inc);
        }
        if (node->left->val - 1 == node->val && node->val - 1 == node->right->val) {
            *best = maxInt(*best, leftLengths.inc + 1 + rightLengths.dec);
        }
    }

    *best = maxInt(*best, maxInt(inc, dec));
    SequenceLengths result = {inc, dec};
    return result;
}

int longestConsecutive(struct TreeNode* root) {
    int best = 0;
    dfs(root, &best);
    return best;
}
