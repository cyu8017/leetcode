// LeetCode 0588 - Design In-Memory File System
// https://leetcode.com/problems/design-in-memory-file-system/

#include <map>
#include <sstream>
#include <string>
#include <vector>

class FileSystem {
    struct Node {
        bool isFile = false;
        std::string content;
        std::map<std::string, Node*> children;
    };

    Node* root;

    std::vector<std::string> split(const std::string& path) {
        std::vector<std::string> parts;
        std::stringstream ss(path);
        std::string part;
        while (std::getline(ss, part, '/')) {
            if (!part.empty()) {
                parts.push_back(part);
            }
        }
        return parts;
    }

public:
    FileSystem() : root(new Node()) {}

    std::vector<std::string> ls(std::string path) {
        if (path == "/") {
            std::vector<std::string> names;
            for (const auto& [name, _] : root->children) {
                names.push_back(name);
            }
            return names;
        }

        std::vector<std::string> parts = split(path);
        Node* node = root;
        for (const std::string& part : parts) {
            node = node->children[part];
        }

        if (node->isFile) {
            return {parts.back()};
        }

        std::vector<std::string> names;
        for (const auto& [name, _] : node->children) {
            names.push_back(name);
        }
        return names;
    }

    void mkdir(std::string path) {
        Node* node = root;
        for (const std::string& part : split(path)) {
            if (!node->children.count(part)) {
                node->children[part] = new Node();
            }
            node = node->children[part];
        }
    }

    void addContentToFile(std::string filePath, std::string content) {
        std::vector<std::string> parts = split(filePath);
        Node* node = root;
        for (size_t i = 0; i + 1 < parts.size(); ++i) {
            if (!node->children.count(parts[i])) {
                node->children[parts[i]] = new Node();
            }
            node = node->children[parts[i]];
        }
        const std::string& name = parts.back();
        if (!node->children.count(name)) {
            node->children[name] = new Node();
            node->children[name]->isFile = true;
        }
        node->children[name]->content += content;
    }

    std::string readContentFromFile(std::string filePath) {
        Node* node = root;
        for (const std::string& part : split(filePath)) {
            node = node->children[part];
        }
        return node->content;
    }
};
