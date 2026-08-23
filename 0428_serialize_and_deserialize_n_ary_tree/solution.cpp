// LeetCode 0428 - Serialize and Deserialize N-ary Tree
// https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

#include <queue>
#include <sstream>
#include <string>
#include <vector>

class Node {
public:
    int val;
    std::vector<Node*> children;
    Node() : val(0) {}
    explicit Node(int _val) : val(_val) {}
    Node(int _val, std::vector<Node*> _children) : val(_val), children(std::move(_children)) {}
};

class Codec {
public:
    std::string encode(Node* root) {
        if (root == nullptr) {
            return "";
        }

        std::vector<std::string> parts;
        std::queue<Node*> queue;
        queue.push(root);

        while (!queue.empty()) {
            Node* node = queue.front();
            queue.pop();
            parts.push_back(std::to_string(node->val));
            parts.push_back(std::to_string(node->children.size()));
            for (Node* child : node->children) {
                parts.push_back(std::to_string(child->val));
                queue.push(child);
            }
        }

        std::ostringstream encoded;
        for (size_t index = 0; index < parts.size(); ++index) {
            if (index > 0) {
                encoded << ',';
            }
            encoded << parts[index];
        }
        return encoded.str();
    }

    Node* decode(std::string data) {
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
        auto readRoot = [&]() -> Node* {
            int value = std::stoi(values[index]);
            int childCount = std::stoi(values[index + 1]);
            index += 2;
            Node* node = new Node(value);
            for (int child = 0; child < childCount; ++child) {
                node->children.push_back(new Node(std::stoi(values[index])));
                ++index;
            }
            return node;
        };

        Node* root = readRoot();
        std::queue<Node*> queue;
        for (Node* child : root->children) {
            queue.push(child);
        }

        while (!queue.empty()) {
            Node* node = queue.front();
            queue.pop();
            int value = std::stoi(values[index]);
            int childCount = std::stoi(values[index + 1]);
            index += 2;
            if (value != node->val) {
                return nullptr;
            }
            for (int child = 0; child < childCount; ++child) {
                Node* childNode = new Node(std::stoi(values[index]));
                node->children.push_back(childNode);
                queue.push(childNode);
                ++index;
            }
        }

        return root;
    }
};
