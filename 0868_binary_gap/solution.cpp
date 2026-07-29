// LeetCode 0868 - Binary Gap
// https://leetcode.com/problems/binary-gap/

#include <algorithm>

class Solution {
public:
    int binaryGap(int n) {
        int last = -1, ans = 0, bit = 0;
        while (n) {
            if (n & 1) {
                if (last != -1) {
                    ans = std::max(ans, bit - last);
                }
                last = bit;
            }
            n >>= 1;
            ++bit;
        }
        return ans;
    }
};
