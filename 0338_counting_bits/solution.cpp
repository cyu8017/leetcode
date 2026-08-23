// LeetCode 0338 - Counting Bits
// https://leetcode.com/problems/counting-bits/

#include <vector>

class Solution {
public:
    std::vector<int> countBits(int n) {
        std::vector<int> result(n + 1, 0);
        for (int index = 1; index <= n; index++) {
            result[index] = result[index & (index - 1)] + 1;
        }
        return result;
    }
};
