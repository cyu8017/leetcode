// LeetCode 1540 - Can Convert String in K Moves
// https://leetcode.com/problems/can-convert-string-in-k-moves/

#include <string>
#include <vector>

class Solution {
public:
    bool canConvertString(std::string s, std::string t, int k) {
        if (s.size() != t.size()) {
            return false;
        }
        std::vector<int> used(26, 0);
        for (std::size_t i = 0; i < s.size(); ++i) {
            int shift = (t[i] - s[i] + 26) % 26;
            if (shift) {
                used[shift] += 1;
                if (shift + 26 * (used[shift] - 1) > k) {
                    return false;
                }
            }
        }
        return true;
    }
};
