// LeetCode 3210 - Find the Encrypted String
// https://leetcode.com/problems/find-the-encrypted-string/

#include <string>

class Solution {
public:
    std::string getEncryptedString(std::string s, int k) {
        int n = (int)s.size();
        std::string cs = s;
        for (int i = 0; i < n; i++) cs[i] = s[(i + k) % n];
        return cs;
    }
};
