// LeetCode 0717 - 1-bit and 2-bit Characters
// https://leetcode.com/problems/1-bit-and-2-bit-characters/

#include <vector>

class Solution {
public:
    bool isOneBitCharacter(std::vector<int>& bits) {
        int i = 0;
        int n = static_cast<int>(bits.size());
        while (i < n - 1) {
            i += bits[i] == 1 ? 2 : 1;
        }
        return i == n - 1;
    }
};
