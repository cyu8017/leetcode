// LeetCode 3516 - Find Closest Person
// https://leetcode.com/problems/find-closest-person/

#include <cstdlib>

class Solution {
public:
    int findClosest(int x, int y, int z) {
        int a = std::abs(x - z), b = std::abs(y - z);
        if (a == b) return 0;
        return a < b ? 1 : 2;
    }
};
