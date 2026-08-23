// LeetCode 2683 - Neighboring Bitwise XOR
// https://leetcode.com/problems/neighboring-bitwise-xor/

#include <vector>

class Solution {
public:
    bool doesValidArrayExist(std::vector<int>& derived) {
        int x = 0;
        for (int v : derived) x ^= v;
        return x == 0;
    }
};
