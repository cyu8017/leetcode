// LeetCode 3513 - Number of Unique XOR Triplets I
// https://leetcode.com/problems/number-of-unique-xor-triplets-i/

#include <vector>
#include <bit>

class Solution {
public:
    int uniqueXorTriplets(std::vector<int>& nums) {
        int n = (int)nums.size();
        if (n <= 2) return n;
        unsigned x = (unsigned)n;
        int len = 0;
        while (x) { len++; x >>= 1; }
        return 1 << len;
    }
};
