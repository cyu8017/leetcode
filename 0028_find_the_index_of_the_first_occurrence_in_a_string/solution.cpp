// LeetCode 0028 - Find the Index of the First Occurrence in a String
// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

#include <string>

class Solution {
public:
    int strStr(std::string haystack, std::string needle) {
        if (needle.empty()) {
            return 0;
        }

        int needleLen = static_cast<int>(needle.size());
        for (int i = 0; i <= static_cast<int>(haystack.size()) - needleLen; i++) {
            if (haystack.compare(i, needleLen, needle) == 0) {
                return i;
            }
        }

        return -1;
    }
};
