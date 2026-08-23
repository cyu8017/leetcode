// LeetCode 3746 - Minimum String Length After Balanced Removals
// https://leetcode.com/problems/minimum-string-length-after-balanced-removals/

#include <cstdlib>
#include <string>

class Solution {
public:
    int minLengthAfterRemovals(std::string s) {
        int a = 0;
        for (char c : s) if (c == 'a') a++;
        int b = (int)s.size() - a;
        return std::abs(a - b);
    }
};
