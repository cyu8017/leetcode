// LeetCode 3232 - Find if Digit Game Can Be Won
// https://leetcode.com/problems/find-if-digit-game-can-be-won/

#include <vector>

class Solution {
public:
    bool canAliceWin(std::vector<int>& nums) {
        int a = 0, b = 0;
        for (int x : nums) {
            if (x < 10) a += x;
            else b += x;
        }
        return a != b;
    }
};
