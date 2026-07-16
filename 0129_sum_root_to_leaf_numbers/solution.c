// LeetCode 0129 - Sum Root to Leaf Numbers
// https://leetcode.com/problems/sum-root-to-leaf-numbers/

static int sumDfs(struct TreeNode* node,int value){if(!node)return 0;value=value*10+node->val;if(!node->left&&!node->right)return value;return sumDfs(node->left,value)+sumDfs(node->right,value);}
int sumNumbers(struct TreeNode* root) { return sumDfs(root,0); }