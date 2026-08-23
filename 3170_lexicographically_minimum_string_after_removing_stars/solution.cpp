// LeetCode 3170 - Lexicographically Minimum String After Removing Stars
// https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

#include <string>
#include <vector>

class Solution {
public:
    std::string clearStars(std::string s) {
        std::vector<std::vector<int>> g(26);
        int n = (int)s.size();
        std::vector<bool> rem(n);
        for (int i = 0; i < n; i++) {
            if (s[i] == '*') {
                rem[i] = true;
                for (int j = 0; j < 26; j++) {
                    if (!g[j].empty()) {
                        rem[g[j].back()] = true;
                        g[j].pop_back();
                        break;
                    }
                }
            } else {
                g[s[i] - 'a'].push_back(i);
            }
        }
        std::string ans;
        for (int i = 0; i < n; i++) if (!rem[i]) ans.push_back(s[i]);
        return ans;
    }
};
