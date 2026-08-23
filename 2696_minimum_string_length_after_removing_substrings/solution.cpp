// LeetCode 2696 - Minimum String Length After Removing Substrings
// https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

#include <string>

class Solution {
public:
    int minLength(std::string s) {
        std::string st;
        for (char c : s) {
            if (!st.empty() && ((st.back() == 'A' && c == 'B') || (st.back() == 'C' && c == 'D')))
                st.pop_back();
            else st.push_back(c);
        }
        return (int)st.size();
    }
};
