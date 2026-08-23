// LeetCode 2839 - Check if Strings Can be Made Equal With Operations I
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

#include <algorithm>
#include <string>

class Solution {
public:
    bool canBeEqual(std::string s1, std::string s2) {
        std::string a{s1[0], s1[2]}, b{s2[0], s2[2]}, c{s1[1], s1[3]}, d{s2[1], s2[3]};
        std::sort(a.begin(), a.end());
        std::sort(b.begin(), b.end());
        std::sort(c.begin(), c.end());
        std::sort(d.begin(), d.end());
        return a == b && c == d;
    }
};
