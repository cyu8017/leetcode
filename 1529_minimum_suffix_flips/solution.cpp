// LeetCode 1529 - Minimum Suffix Flips
// https://leetcode.com/problems/minimum-suffix-flips/

#include <string>

class Solution {
public:
    int minFlips(std::string target) {
        int answer = 0;
        char prev = '0';
        for (char ch : target) {
            if (prev != ch) {
                answer += 1;
            }
            prev = ch;
        }
        return answer;
    }
};
