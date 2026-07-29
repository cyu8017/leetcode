// LeetCode 1576 - Replace All ?'s to Avoid Consecutive Repeating Characters
// https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

#include <string>

class Solution {
public:
    std::string modifyString(std::string s) {
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            if (s[i] == '?') {
                for (char c : {'a', 'b', 'c'}) {
                    if ((i == 0 || s[i - 1] != c) &&
                        (i + 1 == static_cast<int>(s.size()) || s[i + 1] != c)) {
                        s[i] = c;
                        break;
                    }
                }
            }
        }
        return s;
    }
};
