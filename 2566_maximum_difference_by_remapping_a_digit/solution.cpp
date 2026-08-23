// LeetCode 2566 - Maximum Difference by Remapping a Digit
// https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

#include <string>

class Solution {
public:
    int minMaxDifference(int num) {
        std::string s = std::to_string(num);
        auto remap = [&](char from, char to) {
            int v = 0;
            for (char c : s) {
                char d = (c == from) ? to : c;
                v = v * 10 + (d - '0');
            }
            return v;
        };
        int maxV = num;
        for (char c : s) {
            if (c != '9') {
                maxV = remap(c, '9');
                break;
            }
        }
        int minV = remap(s[0], '0');
        return maxV - minV;
    }
};
