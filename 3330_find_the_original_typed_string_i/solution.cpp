// LeetCode 3330 - Find the Original Typed String I
// https://leetcode.com/problems/find-the-original-typed-string-i/

#include <string>

class Solution {
public:
    int possibleStringCount(std::string word) {
        int ans = 1;
        for (int i = 1; i < (int)word.size(); i++) {
            if (word[i] == word[i - 1]) ans++;
        }
        return ans;
    }
};
