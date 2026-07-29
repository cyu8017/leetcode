// LeetCode 0953 - Verifying an Alien Dictionary
// https://leetcode.com/problems/verifying-an-alien-dictionary/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    bool isAlienSorted(std::vector<std::string>& words, std::string order) {
        int rank[26];
        for (int i = 0; i < 26; i++) rank[order[i] - 'a'] = i;
        auto lessEq = [&](const std::string& a, const std::string& b) {
            int n = (int)std::min(a.size(), b.size());
            for (int i = 0; i < n; i++) {
                if (rank[a[i] - 'a'] != rank[b[i] - 'a'])
                    return rank[a[i] - 'a'] < rank[b[i] - 'a'];
            }
            return a.size() <= b.size();
        };
        for (int i = 0; i + 1 < (int)words.size(); i++)
            if (!lessEq(words[i], words[i + 1])) return false;
        return true;
    }
};
