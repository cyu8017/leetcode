// LeetCode 0211 - Design Add and Search Words Data Structure
// https://leetcode.com/problems/design-add-and-search-words-data-structure/

#include <array>
#include <string>

class WordDictionary {
    struct TrieNode {
        std::array<TrieNode*, 26> children{};
        bool isWord = false;
    };

    TrieNode* root;

    bool dfs(TrieNode* node, const std::string& word, int index) const {
        if (index == static_cast<int>(word.size())) {
            return node->isWord;
        }
        char c = word[index];
        if (c == '.') {
            for (TrieNode* child : node->children) {
                if (child && dfs(child, word, index + 1)) {
                    return true;
                }
            }
            return false;
        }
        TrieNode* next = node->children[c - 'a'];
        if (!next) {
            return false;
        }
        return dfs(next, word, index + 1);
    }

public:
    WordDictionary() : root(new TrieNode()) {}

    void addWord(std::string word) {
        TrieNode* node = root;
        for (char c : word) {
            TrieNode*& child = node->children[c - 'a'];
            if (!child) {
                child = new TrieNode();
            }
            node = child;
        }
        node->isWord = true;
    }

    bool search(std::string word) {
        return dfs(root, word, 0);
    }
};
