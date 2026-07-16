// LeetCode 0249 - Group Shifted Strings
// https://leetcode.com/problems/group-shifted-strings/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::vector<std::string>> groupStrings(std::vector<std::string>& strings) {
        std::unordered_map<std::string, std::vector<std::string>> groups;
        std::vector<std::string> order;

        for (const std::string& text : strings) {
            std::string key;
            if (text.empty()) {
                key = "";
            } else {
                int base = text[0];
                for (size_t index = 0; index < text.size(); index++) {
                    if (index > 0) {
                        key.push_back(',');
                    }
                    key += std::to_string((text[index] - base + 26) % 26);
                }
            }
            if (!groups.count(key)) {
                order.push_back(key);
            }
            groups[key].push_back(text);
        }

        std::vector<std::vector<std::string>> result;
        for (const std::string& key : order) {
            result.push_back(groups[key]);
        }
        return result;
    }
};
