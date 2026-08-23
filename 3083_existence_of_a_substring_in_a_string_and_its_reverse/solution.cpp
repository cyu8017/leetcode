// LeetCode 3083 - Existence of a Substring in a String and Its Reverse
// https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

#include <string>

class Solution {
public:
    bool isSubstringPresent(std::string s) {
        bool st[26][26] = {};
        for (int i = 0; i + 1 < (int)s.size(); i++)
            st[s[i + 1] - 'a'][s[i] - 'a'] = true;
        for (int i = 0; i + 1 < (int)s.size(); i++)
            if (st[s[i] - 'a'][s[i + 1] - 'a']) return true;
        return false;
    }
};
