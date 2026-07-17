// LeetCode 1790 - Check if One String Swap Can Make Strings Equal
// https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

#include <string>
#include <vector>

class Solution {
public:
    bool areAlmostEqual(std::string s1, std::string s2) {
        std::vector<int> diff;
        for (int i = 0; i < (int)s1.size(); i++) {
            if (s1[i] != s2[i]) diff.push_back(i);
        }
        if (diff.empty()) return true;
        return diff.size() == 2
            && s1[diff[0]] == s2[diff[1]]
            && s1[diff[1]] == s2[diff[0]];
    }
};
