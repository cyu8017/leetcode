// LeetCode 1807 - Evaluate the Bracket Pairs of a String
// https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::string evaluate(std::string s, const std::vector<std::vector<std::string>>& knowledge) {
        std::unordered_map<std::string, std::string> lookup;
        for (const auto& pair : knowledge) {
            lookup[pair[0]] = pair[1];
        }
        std::string result;
        int n = static_cast<int>(s.size());
        for (int i = 0; i < n;) {
            if (s[i] == '(') {
                int j = i + 1;
                while (j < n && s[j] != ')') {
                    ++j;
                }
                std::string key = s.substr(i + 1, j - i - 1);
                auto it = lookup.find(key);
                result += it == lookup.end() ? "?" : it->second;
                i = j + 1;
            } else {
                result.push_back(s[i]);
                ++i;
            }
        }
        return result;
    }
};
