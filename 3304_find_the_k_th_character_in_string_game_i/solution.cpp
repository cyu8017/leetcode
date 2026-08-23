// LeetCode 3304 - Find the K-th Character in String Game I
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

#include <string>

class Solution {
public:
    char kthCharacter(int k) {
        std::string s = "a";
        while ((int)s.size() < k) {
            int n = (int)s.size();
            for (int i = 0; i < n; i++) s.push_back(char('a' + ((s[i] - 'a' + 1) % 26)));
        }
        return s[k - 1];
    }
};
