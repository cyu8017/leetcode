// LeetCode 0672 - Bulb Switcher II
// https://leetcode.com/problems/bulb-switcher-ii/

#include <algorithm>

class Solution {
public:
    int flipLights(int n, int presses) {
        n = std::min(n, 3);
        if (presses == 0) {
            return 1;
        }
        static const int onePress[] = {2, 3, 4};
        static const int twoPress[] = {2, 4, 7};
        static const int manyPress[] = {2, 4, 8};
        if (presses == 1) {
            return onePress[n - 1];
        }
        if (presses == 2) {
            return twoPress[n - 1];
        }
        return manyPress[n - 1];
    }
};
