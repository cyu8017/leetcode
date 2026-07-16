// LeetCode 0058 - Length of Last Word
// https://leetcode.com/problems/length-of-last-word/

#include <string>

class Solution {
public:
    int lengthOfLastWord(std::string s) {
        int length = 0;
        int i = static_cast<int>(s.size()) - 1;

        while (i >= 0 && s[i] == ' ') {
            --i;
        }

        while (i >= 0 && s[i] != ' ') {
            ++length;
            --i;
        }

        return length;
    }
};
