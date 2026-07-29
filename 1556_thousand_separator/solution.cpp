// LeetCode 1556 - Thousand Separator
// https://leetcode.com/problems/thousand-separator/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::string thousandSeparator(int n) {
        std::string s = std::to_string(n);
        std::vector<std::string> parts;
        while (!s.empty()) {
            if (s.size() <= 3) {
                parts.push_back(s);
                break;
            }
            parts.push_back(s.substr(s.size() - 3));
            s = s.substr(0, s.size() - 3);
        }
        std::reverse(parts.begin(), parts.end());
        std::string result = parts[0];
        for (std::size_t i = 1; i < parts.size(); ++i) {
            result += '.';
            result += parts[i];
        }
        return result;
    }
};
