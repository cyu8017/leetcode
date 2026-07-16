struct TreeNode{int val;TreeNode*left;TreeNode*right;};
class Solution{public:TreeNode* upsideDownBinaryTree(TreeNode*r){TreeNode*p=nullptr,*pr=nullptr;while(r){TreeNode*n=r->left;r->left=pr;pr=r->right;r->right=p;p=r;r=n;}return p;}};
