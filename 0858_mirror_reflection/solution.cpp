// LeetCode 0858 - Mirror Reflection
// https://leetcode.com/problems/mirror-reflection/

#include <numeric>

class Solution {
public:
    int mirrorReflection(int p, int q) {
        int g = std::gcd(p, q);
        p /= g;
        q /= g;
        if (p % 2 == 0) {
            return 2;
        }
        if (q % 2 == 0) {
            return 0;
        }
        return 1;
    }
};
