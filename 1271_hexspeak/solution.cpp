// LeetCode 1271 - Hexspeak
// https://leetcode.com/problems/hexspeak/

#include <string>

class Solution {
public:
    std::string toHexspeak(std::string num) {
        long long value = std::stoll(num);
        const char* digits = "0123456789ABCDEF";
        std::string out;
        while (value) {
            int rem = static_cast<int>(value % 16);
            value /= 16;
            if (rem >= 2 && rem <= 9) {
                return "ERROR";
            }
            out.insert(out.begin(), digits[rem]);
        }
        if (out.empty()) {
            out = "0";
        }
        for (char& ch : out) {
            if (ch == '0') {
                ch = 'O';
            } else if (ch == '1') {
                ch = 'I';
            }
        }
        return out;
    }
};
