#include <vector>
#include <algorithm>
struct TreeNode{int val;TreeNode*left,*right;};class Solution{public:std::vector<int> postorderTraversal(TreeNode*r){std::vector<int>a;if(r){std::vector<TreeNode*>s{r};while(!s.empty()){auto*n=s.back();s.pop_back();a.push_back(n->val);if(n->left)s.push_back(n->left);if(n->right)s.push_back(n->right);}std::reverse(a.begin(),a.end());}return a;}};
