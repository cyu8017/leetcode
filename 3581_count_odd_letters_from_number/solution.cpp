// LeetCode 3581 - Count Odd Letters from Number
// https://leetcode.com/problems/count-odd-letters-from-number/

#include <string>
#include <unordered_map>

class Solution {
public:
    int countOddLetters(int n) {
        static const std::unordered_map<int, std::string> d = {
            {0, "zero"}, {1, "one"}, {2, "two"}, {3, "three"}, {4, "four"},
            {5, "five"}, {6, "six"}, {7, "seven"}, {8, "eight"}, {9, "nine"},
        };
        unsigned mask = 0;
        while (n > 0) {
            int x = n % 10;
            n /= 10;
            for (char c : d.at(x)) mask ^= 1u << (c - 'a');
        }
        return __builtin_popcount(mask);
    }
};
