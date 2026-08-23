// LeetCode 2828 - Check if a String Is an Acronym of Words
// https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

#include <string>
#include <vector>

class Solution {
public:
    bool isAcronym(std::vector<std::string>& words, std::string s) {
        if (words.size() != s.size()) return false;
        for (int i = 0; i < (int)words.size(); i++) {
            if (words[i].empty() || words[i][0] != s[i]) return false;
        }
        return true;
    }
};
