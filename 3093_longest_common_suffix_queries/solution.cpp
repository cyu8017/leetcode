// LeetCode 3093 - Longest Common Suffix Queries
// https://leetcode.com/problems/longest-common-suffix-queries/

#include <string>
#include <vector>

class Solution {
    static const int INF = 1 << 30;
    struct Trie {
        Trie* children[26] = {};
        int length = INF;
        int idx = INF;
    };
    static void insert(Trie* t, const std::string& w, int i) {
        Trie* node = t;
        if (node->length > (int)w.size()) {
            node->length = (int)w.size();
            node->idx = i;
        }
        for (int k = (int)w.size() - 1; k >= 0; k--) {
            int id = w[k] - 'a';
            if (!node->children[id]) node->children[id] = new Trie();
            node = node->children[id];
            if (node->length > (int)w.size()) {
                node->length = (int)w.size();
                node->idx = i;
            }
        }
    }
    static int query(Trie* t, const std::string& w) {
        Trie* node = t;
        for (int k = (int)w.size() - 1; k >= 0; k--) {
            int id = w[k] - 'a';
            if (!node->children[id]) break;
            node = node->children[id];
        }
        return node->idx;
    }
public:
    std::vector<int> stringIndices(std::vector<std::string>& wordsContainer, std::vector<std::string>& wordsQuery) {
        Trie* trie = new Trie();
        for (int i = 0; i < (int)wordsContainer.size(); i++) insert(trie, wordsContainer[i], i);
        std::vector<int> ans;
        for (auto& w : wordsQuery) ans.push_back(query(trie, w));
        return ans;
    }
};
