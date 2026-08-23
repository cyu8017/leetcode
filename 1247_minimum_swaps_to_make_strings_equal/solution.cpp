// LeetCode 1247 - Minimum Swaps to Make Strings Equal
// https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

#include <string>

class Solution {
public:
    int minimumSwap(std::string s1, std::string s2) {
        int xy = 0, yx = 0;
        for (int i = 0; i < static_cast<int>(s1.size()); ++i) {
            if (s1[i] == 'x' && s2[i] == 'y') {
                ++xy;
            } else if (s1[i] == 'y' && s2[i] == 'x') {
                ++yx;
            }
        }
        if ((xy + yx) % 2) {
            return -1;
        }
        return xy / 2 + yx / 2 + 2 * (xy % 2);
    }
};
