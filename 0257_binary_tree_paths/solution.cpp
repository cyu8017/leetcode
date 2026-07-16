// LeetCode 0257 - Binary Tree Paths
// https://leetcode.com/problems/binary-tree-paths/

#include <string>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> result;
        vector<string> path;
        dfs(root, path, result);
        return result;
    }

private:
    void dfs(TreeNode* node, vector<string>& path, vector<string>& result) {
        if (!node) {
            return;
        }
        path.push_back(to_string(node->val));
        if (!node->left && !node->right) {
            string joined;
            for (size_t i = 0; i < path.size(); ++i) {
                if (i > 0) {
                    joined += "->";
                }
                joined += path[i];
            }
            result.push_back(joined);
        } else {
            dfs(node->left, path, result);
            dfs(node->right, path, result);
        }
        path.pop_back();
    }
};
