// LeetCode 3045 - Count Prefix and Suffix Pairs II
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
    struct Node {
        std::unordered_map<int, Node*> children;
        int cnt = 0;
    };
public:
    long long countPrefixSuffixPairs(std::vector<std::string>& words) {
        Node* trie = new Node();
        long long ans = 0;
        for (auto& s : words) {
            Node* node = trie;
            int m = (int)s.size();
            for (int i = 0; i < m; i++) {
                int p = (int)s[i] * 32 + (int)s[m - i - 1];
                if (!node->children.count(p)) node->children[p] = new Node();
                node = node->children[p];
                ans += node->cnt;
            }
            node->cnt++;
        }
        return ans;
    }
};
