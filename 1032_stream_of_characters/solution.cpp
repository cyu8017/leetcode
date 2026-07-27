// LeetCode 1032 - Stream of Characters
// https://leetcode.com/problems/stream-of-characters/

#include <array>
#include <string>
#include <vector>

class StreamChecker {
    struct Node {
        std::array<Node*, 26> children{};
        bool isWord = false;
    };

    Node* root;
    std::string stream;

public:
    StreamChecker(std::vector<std::string>& words) : root(new Node()) {
        for (const auto& word : words) {
            Node* node = root;
            for (int i = static_cast<int>(word.size()) - 1; i >= 0; --i) {
                int idx = word[i] - 'a';
                if (!node->children[idx]) node->children[idx] = new Node();
                node = node->children[idx];
            }
            node->isWord = true;
        }
    }

    bool query(char letter) {
        stream.push_back(letter);
        Node* node = root;
        for (int i = static_cast<int>(stream.size()) - 1; i >= 0; --i) {
            if (node->isWord) return true;
            int idx = stream[i] - 'a';
            if (!node->children[idx]) return false;
            node = node->children[idx];
        }
        return node->isWord;
    }
};

