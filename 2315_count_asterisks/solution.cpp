// LeetCode 2315 - Count Asterisks
// https://leetcode.com/problems/count-asterisks/

#include <string>

class Solution {
public:
    int countAsterisks(std::string s) {
        int ans = 0;
        bool inside = false;
        for (char c : s) {
            if (c == '|') inside = !inside;
            else if (c == '*' && !inside) ans++;
        }
        return ans;
    }
};
