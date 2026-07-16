#include <vector>
struct TreeNode{int val;TreeNode*left,*right;};class Solution{public:std::vector<int> preorderTraversal(TreeNode*r){std::vector<int>a;if(r){std::vector<TreeNode*>s{r};while(!s.empty()){auto*n=s.back();s.pop_back();a.push_back(n->val);if(n->right)s.push_back(n->right);if(n->left)s.push_back(n->left);}}return a;}};
