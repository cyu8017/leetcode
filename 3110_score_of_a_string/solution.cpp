// LeetCode 3110 - Score of a String
// https://leetcode.com/problems/score-of-a-string/

#include <cstdlib>
#include <string>

class Solution {
public:
    int scoreOfString(std::string s) {
        int ans = 0;
        for (int i = 1; i < (int)s.size(); i++)
            ans += std::abs((int)s[i - 1] - (int)s[i]);
        return ans;
    }
};
