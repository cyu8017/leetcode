// LeetCode 3598 - Longest Common Prefix Between Adjacent Strings After Removals
// https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/

#include <algorithm>
#include <map>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> longestCommonPrefix(std::vector<std::string>& words) {
        int n = (int)words.size();
        std::map<int, int> tm;
        auto calc = [&](const std::string& s, const std::string& t) {
            int m = std::min((int)s.size(), (int)t.size());
            for (int k = 0; k < m; k++)
                if (s[k] != t[k]) return k;
            return m;
        };
        auto add = [&](int i, int j) {
            if (i >= 0 && i < n && j >= 0 && j < n) tm[calc(words[i], words[j])]++;
        };
        auto remove = [&](int i, int j) {
            if (i >= 0 && i < n && j >= 0 && j < n) {
                int x = calc(words[i], words[j]);
                if (--tm[x] == 0) tm.erase(x);
            }
        };
        for (int i = 0; i + 1 < n; i++) add(i, i + 1);
        std::vector<int> ans(n);
        for (int i = 0; i < n; i++) {
            remove(i, i + 1);
            remove(i - 1, i);
            add(i - 1, i + 1);
            if (!tm.empty() && tm.rbegin()->first > 0) ans[i] = tm.rbegin()->first;
            remove(i - 1, i + 1);
            add(i - 1, i);
            add(i, i + 1);
        }
        return ans;
    }
};
