// LeetCode 2425 - Bitwise XOR of All Pairings
// https://leetcode.com/problems/bitwise-xor-of-all-pairings/

#include <vector>

class Solution {
public:
    int xorAllNums(std::vector<int>& nums1, std::vector<int>& nums2) {
        int ans = 0;
        if (nums2.size() % 2 == 1) {
            for (int x : nums1) ans ^= x;
        }
        if (nums1.size() % 2 == 1) {
            for (int x : nums2) ans ^= x;
        }
        return ans;
    }
};
