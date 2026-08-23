// LeetCode 3481 - Apply Substitutions
// https://leetcode.com/problems/apply-substitutions/

#include <string>
#include <vector>
#include <unordered_map>

class Solution {
public:
    std::string applySubstitutions(std::vector<std::vector<std::string>>& replacements, std::string text) {
        std::unordered_map<std::string, std::string> mp;
        for (auto& r : replacements) mp[r[0]] = r[1];
        auto resolve = [&](auto&& self, const std::string& s) -> std::string {
            std::string out;
            for (int i = 0; i < (int)s.size();) {
                if (s[i] == '%') {
                    int j = i + 1;
                    while (j < (int)s.size() && s[j] != '%') j++;
                    std::string key = s.substr(i + 1, j - i - 1);
                    out += self(self, mp[key]);
                    i = j + 1;
                } else {
                    out.push_back(s[i]);
                    i++;
                }
            }
            return out;
        };
        return resolve(resolve, text);
    }
};
