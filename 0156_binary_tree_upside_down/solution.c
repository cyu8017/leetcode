struct TreeNode{int val;struct TreeNode*left;struct TreeNode*right;};
#include <stddef.h>
struct TreeNode* upsideDownBinaryTree(struct TreeNode*r){struct TreeNode*p=0,*q=0;while(r){struct TreeNode*n=r->left;r->left=q;q=r->right;r->right=p;p=r;r=n;}return p;}
