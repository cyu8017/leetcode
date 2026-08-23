// LeetCode 0810 - Chalkboard XOR Game
// https://leetcode.com/problems/chalkboard-xor-game/

#include <vector>

class Solution {
public:
    bool xorGame(std::vector<int>& nums) {
        int x = 0;
        for (int num : nums) {
            x ^= num;
        }
        return x == 0 || nums.size() % 2 == 0;
    }
};
