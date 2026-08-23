// LeetCode 1256 - Encode Number
// https://leetcode.com/problems/encode-number/

#include <bitset>
#include <string>

class Solution {
public:
    std::string encode(int num) {
        std::string binary = std::bitset<32>(num + 1).to_string();
        auto pos = binary.find('1');
        if (pos == std::string::npos) {
            return "";
        }
        return binary.substr(pos + 1);
    }
};
