// LeetCode 1805 - Number of Different Integers in a String
// https://leetcode.com/problems/number-of-different-integers-in-a-string/

#include <cctype>
#include <string>
#include <unordered_set>

class Solution {
public:
    int numDifferentIntegers(std::string word) {
        std::unordered_set<std::string> seen;
        int n = static_cast<int>(word.size());
        for (int i = 0; i < n;) {
            if (!std::isdigit(static_cast<unsigned char>(word[i]))) {
                ++i;
                continue;
            }
            int j = i;
            while (j < n && std::isdigit(static_cast<unsigned char>(word[j]))) {
                ++j;
            }
            int start = i;
            while (start + 1 < j && word[start] == '0') {
                ++start;
            }
            seen.insert(word.substr(start, j - start));
            i = j;
        }
        return static_cast<int>(seen.size());
    }
};
