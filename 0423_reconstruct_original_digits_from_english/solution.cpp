// LeetCode 0423 - Reconstruct Original Digits from English
// https://leetcode.com/problems/reconstruct-original-digits-from-english/

#include <string>

class Solution {
public:
    std::string originalDigits(std::string s) {
        int counts[26] = {};
        for (char ch : s) {
            ++counts[ch - 'a'];
        }

        int digitCounts[10] = {};
        digitCounts[0] = counts['z' - 'a'];
        digitCounts[2] = counts['w' - 'a'];
        digitCounts[4] = counts['u' - 'a'];
        digitCounts[6] = counts['x' - 'a'];
        digitCounts[8] = counts['g' - 'a'];
        digitCounts[1] = counts['o' - 'a'] - digitCounts[0] - digitCounts[2] - digitCounts[4];
        digitCounts[3] = counts['h' - 'a'] - digitCounts[8];
        digitCounts[5] = counts['f' - 'a'] - digitCounts[4];
        digitCounts[7] = counts['s' - 'a'] - digitCounts[6];
        digitCounts[9] = counts['i' - 'a'] - digitCounts[5] - digitCounts[6] - digitCounts[8];

        std::string result;
        for (int digit = 0; digit < 10; ++digit) {
            result.append(digitCounts[digit], static_cast<char>('0' + digit));
        }
        return result;
    }
};
