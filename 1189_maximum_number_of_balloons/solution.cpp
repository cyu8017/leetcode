// LeetCode 1189 - Maximum Number of Balloons
// https://leetcode.com/problems/maximum-number-of-balloons/

#include <algorithm>
#include <string>

class Solution {
public:
    int maxNumberOfBalloons(std::string text) {
        int count[26] = {};
        for (char ch : text) ++count[ch - 'a'];
        return std::min({count['b' - 'a'], count['a' - 'a'], count['l' - 'a'] / 2,
                         count['o' - 'a'] / 2, count['n' - 'a']});
    }
};
