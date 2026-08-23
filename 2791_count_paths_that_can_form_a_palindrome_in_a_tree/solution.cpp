// LeetCode 2791 - Count Paths That Can Form a Palindrome in a Tree
// https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    long long countPalindromePaths(std::vector<int>& parent, std::string s) {
        int n = (int)parent.size();
        std::vector<std::vector<int>> g(n);
        for (int i = 1; i < n; i++) g[parent[i]].push_back(i);
        std::unordered_map<int, int> freq;
        freq[0] = 1;
        long long ans = 0;
        auto dfs = [&](auto&& self, int u, int mask) -> void {
            for (int v : g[u]) {
                int nm = mask ^ (1 << (s[v] - 'a'));
                ans += freq[nm];
                for (int b = 0; b < 26; b++) ans += freq[nm ^ (1 << b)];
                freq[nm]++;
                self(self, v, nm);
            }
        };
        dfs(dfs, 0, 0);
        return ans;
    }
};
