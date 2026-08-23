// LeetCode 2849 - Determine if a Cell Is Reachable at a Given Time
// https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

#include <algorithm>
#include <cstdlib>

class Solution {
public:
    bool isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        int need = std::max(std::abs(sx - fx), std::abs(sy - fy));
        if (need == 0) return t != 1;
        return t >= need;
    }
};
