// LeetCode 1624 - Largest Substring Between Two Equal Characters
// https://leetcode.com/problems/largest-substring-between-two-equal-characters/

#include <algorithm>
#include <string>
#include <unordered_map>

class Solution {
public:
    int maxLengthBetweenEqualCharacters(std::string s) {
        std::unordered_map<char, int> first;
        int ans = -1;
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            if (first.count(s[i])) {
                ans = std::max(ans, i - first[s[i]] - 1);
            } else {
                first[s[i]] = i;
            }
        }
        return ans;
    }
};
