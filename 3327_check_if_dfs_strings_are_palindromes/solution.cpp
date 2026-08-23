// LeetCode 3327 - Check DFS Strings Are Palindromes
// https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/

#include <functional>
#include <string>
#include <vector>

class Solution {
    bool isPal(const std::string& s) {
        for (int i = 0, j = (int)s.size() - 1; i < j; i++, j--) {
            if (s[i] != s[j]) return false;
        }
        return true;
    }

public:
    std::vector<bool> findAnswer(std::vector<int>& parent, std::string s) {
        int n = (int)parent.size();
        std::vector<std::vector<int>> g(n);
        for (int i = 1; i < n; i++) g[parent[i]].push_back(i);
        std::vector<bool> ans(n);
        std::function<std::string(int)> dfsStr = [&](int u) -> std::string {
            std::string out;
            for (int v : g[u]) out += dfsStr(v);
            out.push_back(s[u]);
            ans[u] = isPal(out);
            return out;
        };
        dfsStr(0);
        return ans;
    }
};
