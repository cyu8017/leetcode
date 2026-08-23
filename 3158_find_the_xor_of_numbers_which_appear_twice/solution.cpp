// LeetCode 3158 - Find the XOR of Numbers Which Appear Twice
// https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

#include <vector>
#include <array>

class Solution {
public:
    int duplicateNumbersXOR(std::vector<int>& nums) {
        std::array<int, 51> cnt{};
        int ans = 0;
        for (int x : nums) {
            if (++cnt[x] == 2) ans ^= x;
        }
        return ans;
    }
};
