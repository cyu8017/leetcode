// LeetCode 1945 - Sum of Digits of String After Convert
#include <string>

class Solution {
public:
    int getLucky(std::string s, int k) {
        std::string num;
        for (char c : s) num += std::to_string(c - 'a' + 1);
        for (int t = 0; t < k; t++) {
            int sum = 0;
            for (char d : num) sum += d - '0';
            num = std::to_string(sum);
        }
        return std::stoi(num);
    }
};
