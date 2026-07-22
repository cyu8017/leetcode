// LeetCode 1684 - Count the Number of Consistent Strings
// https://leetcode.com/problems/count-the-number-of-consistent-strings/

#include <string>
#include <vector>

class Solution {
public:
    int countConsistentStrings(std::string allowed, std::vector<std::string>& words) {
        bool ok[26] = {};
        for (char c : allowed) {
            ok[c - 'a'] = true;
        }
        int ans = 0;
        for (const auto& w : words) {
            bool good = true;
            for (char c : w) {
                if (!ok[c - 'a']) {
                    good = false;
                    break;
                }
            }
            if (good) {
                ++ans;
            }
        }
        return ans;
    }
};
