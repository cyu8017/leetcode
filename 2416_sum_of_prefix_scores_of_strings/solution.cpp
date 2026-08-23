// LeetCode 2416 - Sum of Prefix Scores of Strings
// https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> sumPrefixScores(std::vector<std::string>& words) {
        struct TrieNode {
            TrieNode* child[26] = {};
            int cnt = 0;
        };
        TrieNode* root = new TrieNode();
        for (auto& w : words) {
            TrieNode* cur = root;
            for (char ch : w) {
                int c = ch - 'a';
                if (!cur->child[c]) cur->child[c] = new TrieNode();
                cur = cur->child[c];
                cur->cnt++;
            }
        }
        std::vector<int> ans(words.size());
        for (int i = 0; i < (int)words.size(); i++) {
            TrieNode* cur = root;
            int sum = 0;
            for (char ch : words[i]) {
                cur = cur->child[ch - 'a'];
                sum += cur->cnt;
            }
            ans[i] = sum;
        }
        return ans;
    }
};
