// LeetCode 3291 - Minimum Number of Valid Strings to Form Target I
// https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/

#include <string>
#include <vector>

class Solution {
    struct TrieNode {
        TrieNode* next[26]{};
    };

public:
    int minValidStrings(std::vector<std::string>& words, std::string target) {
        int n = (int)target.size();
        const int inf = 1000000000;
        std::vector<int> dp(n + 1, inf);
        dp[0] = 0;
        TrieNode* root = new TrieNode();
        for (auto& w : words) {
            TrieNode* cur = root;
            for (char c : w) {
                int ci = c - 'a';
                if (!cur->next[ci]) cur->next[ci] = new TrieNode();
                cur = cur->next[ci];
            }
        }
        for (int i = 0; i < n; i++) {
            if (dp[i] == inf) continue;
            TrieNode* cur = root;
            for (int j = i; j < n; j++) {
                int ci = target[j] - 'a';
                if (!cur->next[ci]) break;
                cur = cur->next[ci];
                if (dp[i] + 1 < dp[j + 1]) dp[j + 1] = dp[i] + 1;
            }
        }
        return dp[n] == inf ? -1 : dp[n];
    }
};
