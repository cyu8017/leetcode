// LeetCode 0124 - Binary Tree Maximum Path Sum
// https://leetcode.com/problems/binary-tree-maximum-path-sum/

static int best;
static int gain(struct TreeNode* node){if(!node)return 0;int l=gain(node->left);int r=gain(node->right);if(l<0)l=0;if(r<0)r=0;if(node->val+l+r>best)best=node->val+l+r;return node->val+(l>r?l:r);}
int maxPathSum(struct TreeNode* root) { best=(-2147483647-1);gain(root);return best; }