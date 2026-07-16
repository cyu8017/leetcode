// LeetCode 0449 - Serialize and Deserialize BST
// https://leetcode.com/problems/serialize-and-deserialize-bst/

#include <functional>
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
        std::vector<std::string> parts;

        std::function<void(TreeNode*)> preorder = [&](TreeNode* node) {
            if (node == nullptr) {
                parts.push_back("#");
                return;
            }
            parts.push_back(std::to_string(node->val));
            preorder(node->left);
            preorder(node->right);
        };

        preorder(root);

        std::ostringstream encoded;
        for (size_t index = 0; index < parts.size(); ++index) {
            if (index > 0) {
                encoded << ',';
            }
            encoded << parts[index];
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

        size_t index = 0;
        std::function<TreeNode*()> build = [&]() -> TreeNode* {
            std::string current = values[index++];
            if (current == "#") {
                return nullptr;
            }
            TreeNode* node = new TreeNode(std::stoi(current));
            node->left = build();
            node->right = build();
            return node;
        };

        return build();
    }
};
