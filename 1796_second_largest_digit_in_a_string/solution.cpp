// LeetCode 1796 - Second Largest Digit in a String
// https://leetcode.com/problems/second-largest-digit-in-a-string/

#include <string>

class Solution {
public:
    int secondHighest(std::string s) {
        int largest = -1;
        int second = -1;
        for (char ch : s) {
            if (ch >= '0' && ch <= '9') {
                int d = ch - '0';
                if (d > largest) {
                    second = largest;
                    largest = d;
                } else if (d < largest && d > second) {
                    second = d;
                }
            }
        }
        return second;
    }
};
