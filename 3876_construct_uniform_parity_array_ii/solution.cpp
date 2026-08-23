// LeetCode 3876 - Construct Uniform Parity Array II
// https://leetcode.com/problems/construct-uniform-parity-array-ii/

#include <climits>
#include <vector>

class Solution {
public:
    bool uniformArray(std::vector<int>& nums1) {
        int mn = INT_MAX;
        for (int x : nums1) {
            if (x % 2 == 1 && x < mn) mn = x;
        }
        for (int x : nums1) {
            if (x % 2 == 0 && mn != INT_MAX && x < mn) return false;
        }
        return true;
    }
};
