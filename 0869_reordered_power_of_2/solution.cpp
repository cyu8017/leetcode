// LeetCode 0869 - Reordered Power of 2
// https://leetcode.com/problems/reordered-power-of-2/

#include <algorithm>
#include <string>

class Solution {
public:
    bool reorderedPowerOf2(int n) {
        auto sig = [](int x) {
            std::string s = std::to_string(x);
            std::sort(s.begin(), s.end());
            return s;
        };
        std::string target = sig(n);
        for (int i = 0; i < 31; ++i) {
            if (sig(1 << i) == target) {
                return true;
            }
        }
        return false;
    }
};
