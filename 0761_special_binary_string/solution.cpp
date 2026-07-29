// LeetCode 0761 - Special Binary String
// https://leetcode.com/problems/special-binary-string/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::string makeLargestSpecial(std::string s) {
        std::vector<std::string> parts;
        int balance = 0;
        int start = 0;
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            balance += s[i] == '1' ? 1 : -1;
            if (balance == 0) {
                parts.push_back("1" + makeLargestSpecial(s.substr(start + 1, i - start - 1)) + "0");
                start = i + 1;
            }
        }
        std::sort(parts.begin(), parts.end(), std::greater<std::string>());
        std::string result;
        for (const std::string& part : parts) {
            result += part;
        }
        return result;
    }
};
