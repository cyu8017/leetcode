// LeetCode 1881 - Maximum Value after Insertion
// https://leetcode.com/problems/maximum-value-after-insertion/

#include <string>

class Solution {
public:
    std::string maxValue(std::string n, int x) {
        bool neg = !n.empty() && n[0] == '-';
        int start = neg ? 1 : 0;
        for (int i = start; i < static_cast<int>(n.size()); i++) {
            int d = n[i] - '0';
            if (neg) {
                if (d > x) {
                    return n.substr(0, i) + std::to_string(x) + n.substr(i);
                }
            } else if (d < x) {
                return n.substr(0, i) + std::to_string(x) + n.substr(i);
            }
        }
        return n + std::to_string(x);
    }
};
