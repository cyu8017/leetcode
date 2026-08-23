// LeetCode 0482 - License Key Formatting
// https://leetcode.com/problems/license-key-formatting/

#include <cctype>
#include <string>

class Solution {
public:
    std::string licenseKeyFormatting(std::string s, int k) {
        std::string chars;
        chars.reserve(s.size());
        for (char ch : s) {
            if (ch != '-') {
                chars.push_back(static_cast<char>(std::toupper(static_cast<unsigned char>(ch))));
            }
        }
        if (chars.empty()) {
            return "";
        }
        const int firstLen = static_cast<int>(chars.size()) % k == 0 ? k : static_cast<int>(chars.size()) % k;
        std::string result = chars.substr(0, firstLen);
        for (int index = firstLen; index < static_cast<int>(chars.size()); index += k) {
            result.push_back('-');
            result.append(chars.substr(index, k));
        }
        return result;
    }
};
