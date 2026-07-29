// LeetCode 1948 - Delete Duplicate Folders in System
#include <map>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
    struct Node {
        std::map<std::string, Node*> children;
    };
    std::unordered_map<std::string, int> dup;
    std::unordered_map<Node*, std::string> serialOf;
    std::string serialize(Node* node) {
        if (!node || node->children.empty()) return "";
        std::string serial;
        for (auto& [name, child] : node->children) {
            serial += name + "(" + serialize(child) + ")";
        }
        if (!serial.empty()) {
            dup[serial]++;
            serialOf[node] = serial;
        }
        return serial;
    }
    void collect(Node* node, std::vector<std::string>& path, std::vector<std::vector<std::string>>& ans) {
        for (auto& [name, child] : node->children) {
            auto it = serialOf.find(child);
            if (it != serialOf.end() && dup[it->second] > 1) continue;
            path.push_back(name);
            ans.push_back(path);
            collect(child, path, ans);
            path.pop_back();
        }
    }
public:
    std::vector<std::vector<std::string>> deleteDuplicateFolder(std::vector<std::vector<std::string>>& paths) {
        Node* root = new Node();
        for (auto& path : paths) {
            Node* cur = root;
            for (auto& folder : path) {
                if (!cur->children.count(folder)) cur->children[folder] = new Node();
                cur = cur->children[folder];
            }
        }
        serialize(root);
        std::vector<std::vector<std::string>> ans;
        std::vector<std::string> path;
        collect(root, path, ans);
        return ans;
    }
};
