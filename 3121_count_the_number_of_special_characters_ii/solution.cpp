// LeetCode 3121 - Count the Number of Special Characters II
// https://leetcode.com/problems/count-the-number-of-special-characters-ii/

#include <string>
#include <vector>

class Solution {
public:
    int numberOfSpecialChars(std::string word) {
        std::vector<int> first(128), last(128);
        for (int i = 0; i < (int)word.size(); i++) {
            unsigned char c = word[i];
            if (first[c] == 0) first[c] = i + 1;
            last[c] = i + 1;
        }
        int ans = 0;
        for (int i = 0; i < 26; i++) {
            if (last['a' + i] > 0 && last['a' + i] < first['A' + i]) ans++;
        }
        return ans;
    }
};
