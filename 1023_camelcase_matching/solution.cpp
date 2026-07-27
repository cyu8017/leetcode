// LeetCode 1023 - Camelcase Matching
// https://leetcode.com/problems/camelcase-matching/

#include <cctype>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<bool> camelMatch(std::vector<std::string>& queries, std::string pattern) {
        auto matches = [&](const std::string& q) {
            int i = 0;
            for (char ch : q) {
                if (i < static_cast<int>(pattern.size()) && ch == pattern[i]) {
                    ++i;
                } else if (std::isupper(static_cast<unsigned char>(ch))) {
                    return false;
                }
            }
            return i == static_cast<int>(pattern.size());
        };
        std::vector<bool> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) ans.push_back(matches(q));
        return ans;
    }
};

