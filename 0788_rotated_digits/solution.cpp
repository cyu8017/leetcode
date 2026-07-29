// LeetCode 0788 - Rotated Digits
// https://leetcode.com/problems/rotated-digits/

#include <string>

class Solution {
public:
    int rotatedDigits(int n) {
        int count = 0;
        for (int num = 1; num <= n; ++num) {
            std::string s = std::to_string(num);
            bool ok = true;
            bool changed = false;
            for (char ch : s) {
                if (ch == '3' || ch == '4' || ch == '7') {
                    ok = false;
                    break;
                }
                if (ch == '2' || ch == '5' || ch == '6' || ch == '9') {
                    changed = true;
                }
            }
            if (ok && changed) {
                ++count;
            }
        }
        return count;
    }
};
