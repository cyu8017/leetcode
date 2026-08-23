// LeetCode 3106 - Lexicographically Smallest String After Operations With Constraint
// https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string getSmallestString(std::string s, int k) {
        for (int i = 0; i < (int)s.size(); i++) {
            char c1 = s[i];
            for (char c2 = 'a'; c2 < c1; c2++) {
                int d = std::min(c1 - c2, 26 - (c1 - c2));
                if (d <= k) {
                    s[i] = c2;
                    k -= d;
                    break;
                }
            }
        }
        return s;
    }
};
