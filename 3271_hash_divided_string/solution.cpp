// LeetCode 3271 - Hash Divided String
// https://leetcode.com/problems/hash-divided-string/

#include <string>

class Solution {
public:
    std::string stringHash(std::string s, int k) {
        std::string out;
        out.reserve(s.size() / k);
        for (int i = 0; i < (int)s.size(); i += k) {
            int sum = 0;
            for (int j = i; j < i + k; j++) sum += s[j] - 'a';
            out.push_back(char('a' + sum % 26));
        }
        return out;
    }
};
