// LeetCode 1087 - Brace Expansion
// https://leetcode.com/problems/brace-expansion/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> expand(std::string s) {
        std::vector<std::vector<std::string>> groups;
        int i = 0;
        int n = static_cast<int>(s.size());
        while (i < n) {
            if (s[i] == '{') {
                int j = static_cast<int>(s.find('}', i));
                std::vector<std::string> group;
                std::string token;
                for (int k = i + 1; k < j; ++k) {
                    if (s[k] == ',') {
                        group.push_back(token);
                        token.clear();
                    } else {
                        token.push_back(s[k]);
                    }
                }
                group.push_back(token);
                std::sort(group.begin(), group.end());
                groups.push_back(group);
                i = j + 1;
            } else {
                groups.push_back({std::string(1, s[i])});
                ++i;
            }
        }
        std::vector<std::string> ans = {""};
        for (const auto& group : groups) {
            std::vector<std::string> next;
            for (const std::string& prefix : ans) {
                for (const std::string& ch : group) {
                    next.push_back(prefix + ch);
                }
            }
            ans.swap(next);
        }
        return ans;
    }
};
