// LeetCode 0208 - Implement Trie (Prefix Tree)
#include <array>
#include <string>
class Trie { struct Node { std::array<Node*, 26> children{}; bool isWord = false; }; Node* root; Node* find(const std::string& text) const { Node* node = root; for (char ch : text) { node = node->children[ch - 'a']; if (!node) return nullptr; } return node; } public: Trie() : root(new Node()) {} void insert(std::string word) { Node* node = root; for (char ch : word) { Node*& child = node->children[ch - 'a']; if (!child) child = new Node(); node = child; } node->isWord = true; } bool search(std::string word) { Node* node = find(word); return node && node->isWord; } bool startsWith(std::string prefix) { return find(prefix) != nullptr; } };
