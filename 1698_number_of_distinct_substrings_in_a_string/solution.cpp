// LeetCode 1698 - Number of Distinct Substrings in a String
// https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/

#include <memory>
#include <string>
#include <unordered_map>

class Solution {
    struct TrieNode {
        std::unordered_map<char, std::unique_ptr<TrieNode>> children;
    };

public:
    int countDistinct(std::string s) {
        TrieNode root;
        int ans = 0;
        for (size_t i = 0; i < s.size(); ++i) {
            TrieNode* node = &root;
            for (size_t j = i; j < s.size(); ++j) {
                char c = s[j];
                auto it = node->children.find(c);
                if (it == node->children.end()) {
                    node->children[c] = std::make_unique<TrieNode>();
                    ++ans;
                    it = node->children.find(c);
                }
                node = it->second.get();
            }
        }
        return ans;
    }
};
