// LeetCode 3019 - Number of Changing Keys
// https://leetcode.com/problems/number-of-changing-keys/

#include <cctype>
#include <string>

class Solution {
public:
    int countKeyChanges(std::string s) {
        for (char& c : s) c = (char)std::tolower((unsigned char)c);
        int ans = 0;
        for (int i = 1; i < (int)s.size(); i++)
            if (s[i] != s[i - 1]) ans++;
        return ans;
    }
};
