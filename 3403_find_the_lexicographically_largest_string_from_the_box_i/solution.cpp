// LeetCode 3403 - Find the Lexicographically Largest String From the Box I
// https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/

#include <string>

class Solution {
public:
    std::string answerString(std::string word, int numFriends) {
        if (numFriends == 1) return word;
        int n = (int)word.size();
        int maxLen = n - (numFriends - 1);
        std::string ans;
        for (int i = 0; i < n; i++) {
            int end = i + maxLen;
            if (end > n) end = n;
            std::string cand = word.substr(i, end - i);
            if (cand > ans) ans = cand;
        }
        return ans;
    }
};
