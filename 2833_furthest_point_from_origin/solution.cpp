// LeetCode 2833 - Furthest Point From Origin
// https://leetcode.com/problems/furthest-point-from-origin/

#include <cstdlib>
#include <string>

class Solution {
public:
    int furthestDistanceFromOrigin(std::string moves) {
        int L = 0, R = 0, u = 0;
        for (char c : moves) {
            if (c == 'L') L++;
            else if (c == 'R') R++;
            else u++;
        }
        return std::abs(L - R) + u;
    }
};
