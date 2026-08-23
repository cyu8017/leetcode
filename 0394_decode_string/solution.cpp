// LeetCode 0394 - Decode String
// https://leetcode.com/problems/decode-string/

#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    std::string decodeString(std::string s) {
        std::vector<std::pair<std::string, int>> stack;
        std::string current;
        int number = 0;

        for (char ch : s) {
            if (ch >= '0' && ch <= '9') {
                number = number * 10 + (ch - '0');
            } else if (ch == '[') {
                stack.emplace_back(current, number);
                current.clear();
                number = 0;
            } else if (ch == ']') {
                auto [previous, count] = stack.back();
                stack.pop_back();
                std::string repeated;
                repeated.reserve(current.size() * static_cast<size_t>(count));
                for (int index = 0; index < count; ++index) {
                    repeated += current;
                }
                current = previous + repeated;
            } else {
                current += ch;
            }
        }

        return current;
    }
};
