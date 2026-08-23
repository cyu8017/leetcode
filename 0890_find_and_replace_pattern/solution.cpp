// LeetCode 0890 - Find and Replace Pattern
// https://leetcode.com/problems/find-and-replace-pattern/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::string> findAndReplacePattern(std::vector<std::string>& words,
                                                   std::string pattern) {
        auto normalize = [](const std::string& s) {
            std::unordered_map<char, int> mapping;
            std::vector<int> out;
            for (char ch : s) {
                if (!mapping.count(ch)) {
                    mapping[ch] = static_cast<int>(mapping.size());
                }
                out.push_back(mapping[ch]);
            }
            return out;
        };
        auto target = normalize(pattern);
        std::vector<std::string> ans;
        for (const auto& w : words) {
            if (normalize(w) == target) {
                ans.push_back(w);
            }
        }
        return ans;
    }
};
