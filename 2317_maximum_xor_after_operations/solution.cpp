// LeetCode 2317 - Maximum XOR After Operations
// https://leetcode.com/problems/maximum-xor-after-operations/

#include <vector>

class Solution {
public:
    int maximumXOR(std::vector<int>& nums) {
        int ans = 0;
        for (int x : nums) ans |= x;
        return ans;
    }
};
