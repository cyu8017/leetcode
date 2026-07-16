// LeetCode 0316 - Remove Duplicate Letters
// https://leetcode.com/problems/remove-duplicate-letters/

#include <string>
#include <vector>

class Solution {
public:
    std::string removeDuplicateLetters(std::string s) {
        std::vector<int> lastIndex(256, -1);
        for (int index = 0; index < static_cast<int>(s.size()); index++) {
            lastIndex[static_cast<unsigned char>(s[index])] = index;
        }

        std::string stack;
        std::vector<bool> seen(256, false);
        for (int index = 0; index < static_cast<int>(s.size()); index++) {
            char character = s[index];
            if (seen[static_cast<unsigned char>(character)]) {
                continue;
            }
            while (!stack.empty()
                && stack.back() > character
                && lastIndex[static_cast<unsigned char>(stack.back())] > index) {
                seen[static_cast<unsigned char>(stack.back())] = false;
                stack.pop_back();
            }
            stack.push_back(character);
            seen[static_cast<unsigned char>(character)] = true;
        }

        return stack;
    }
};
