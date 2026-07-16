// LeetCode 0297 - Serialize and Deserialize Binary Tree
// https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

#include <queue>
#include <sstream>
#include <string>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Codec {
public:
    std::string serialize(TreeNode* root) {
        if (root == nullptr) {
            return "";
        }

        std::vector<std::string> values;
        std::queue<TreeNode*> queue;
        queue.push(root);

        while (!queue.empty()) {
            TreeNode* node = queue.front();
            queue.pop();
            if (node == nullptr) {
                values.push_back("");
            } else {
                values.push_back(std::to_string(node->val));
                queue.push(node->left);
                queue.push(node->right);
            }
        }

        while (!values.empty() && values.back().empty()) {
            values.pop_back();
        }

        std::ostringstream encoded;
        for (size_t index = 0; index < values.size(); index++) {
            if (index > 0) {
                encoded << ',';
            }
            encoded << values[index];
        }
        return encoded.str();
    }

    TreeNode* deserialize(std::string data) {
        if (data.empty()) {
            return nullptr;
        }

        std::vector<std::string> values;
        std::stringstream stream(data);
        std::string token;
        while (std::getline(stream, token, ',')) {
            values.push_back(token);
        }

        TreeNode* root = new TreeNode(std::stoi(values[0]));
        std::queue<TreeNode*> queue;
        queue.push(root);
        size_t index = 1;

        while (!queue.empty() && index < values.size()) {
            TreeNode* node = queue.front();
            queue.pop();

            if (index < values.size() && !values[index].empty()) {
                node->left = new TreeNode(std::stoi(values[index]));
                queue.push(node->left);
            }
            index++;

            if (index < values.size() && !values[index].empty()) {
                node->right = new TreeNode(std::stoi(values[index]));
                queue.push(node->right);
            }
            index++;
        }

        return root;
    }
};
