// LeetCode 1804 - Implement Trie II (Prefix Tree)
// https://leetcode.com/problems/implement-trie-ii-prefix-tree/

#include <string>
#include <unordered_map>

class Trie {
public:
    Trie() : root(new TrieNode()) {}

    void insert(std::string word) {
        TrieNode* node = root;
        for (char ch : word) {
            if (!node->children.count(ch)) {
                node->children[ch] = new TrieNode();
            }
            node = node->children[ch];
            node->prefixCount += 1;
        }
        node->wordCount += 1;
    }

    int countWordsEqualTo(std::string word) {
        TrieNode* node = find(word);
        return node ? node->wordCount : 0;
    }

    int countWordsStartingWith(std::string prefix) {
        TrieNode* node = find(prefix);
        return node ? node->prefixCount : 0;
    }

    void erase(std::string word) {
        TrieNode* node = root;
        for (char ch : word) {
            node = node->children[ch];
            node->prefixCount -= 1;
        }
        node->wordCount -= 1;
    }

private:
    struct TrieNode {
        std::unordered_map<char, TrieNode*> children;
        int wordCount = 0;
        int prefixCount = 0;
    };

    TrieNode* root;

    TrieNode* find(const std::string& text) const {
        TrieNode* node = root;
        for (char ch : text) {
            auto it = node->children.find(ch);
            if (it == node->children.end()) {
                return nullptr;
            }
            node = it->second;
        }
        return node;
    }
};
