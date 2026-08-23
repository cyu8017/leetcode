// LeetCode 3735 - Lexicographically Smallest String After Reverse II
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string lexSmallest(std::string s) {
        int n = (int)s.size();
        std::string best = s;
        for (int i = 1; i <= n; i++) {
            std::string t = s;
            std::reverse(t.begin(), t.begin() + i);
            if (t < best) best = t;
        }
        for (int i = 0; i < n; i++) {
            std::string t = s;
            std::reverse(t.begin() + i, t.end());
            if (t < best) best = t;
        }
        return best;
    }
};
