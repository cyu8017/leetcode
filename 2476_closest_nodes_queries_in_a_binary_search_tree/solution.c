// LeetCode 2476 - Closest Nodes Queries in a Binary Search Tree
// https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static int* vals2476;
static int vc2476, vcap2476;

static void inorder2476(struct TreeNode* node) {
    if (!node) return;
    inorder2476(node->left);
    if (vc2476 == vcap2476) {
        vcap2476 = vcap2476 ? vcap2476 * 2 : 64;
        vals2476 = (int*)realloc(vals2476, (size_t)vcap2476 * sizeof(int));
    }
    vals2476[vc2476++] = node->val;
    inorder2476(node->right);
}

int** closestNodes(struct TreeNode* root, int* queries, int queriesSize, int* returnSize, int** returnColumnSizes) {
    vals2476 = NULL; vc2476 = 0; vcap2476 = 0;
    inorder2476(root);
    int** ans = (int**)malloc((size_t)queriesSize * sizeof(int*));
    int* cols = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        int q = queries[i];
        int lo = 0, hi = vc2476;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (vals2476[mid] < q) lo = mid + 1;
            else hi = mid;
        }
        int mx = (lo < vc2476) ? vals2476[lo] : -1;
        int mn = -1;
        if (lo < vc2476 && vals2476[lo] == q) mn = q;
        else if (lo > 0) mn = vals2476[lo - 1];
        ans[i] = (int*)malloc(2 * sizeof(int));
        ans[i][0] = mn;
        ans[i][1] = mx;
        cols[i] = 2;
    }
    free(vals2476);
    *returnSize = queriesSize;
    *returnColumnSizes = cols;
    return ans;
}
