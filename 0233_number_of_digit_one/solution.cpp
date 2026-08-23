// LeetCode 0233 - Number of Digit One
// https://leetcode.com/problems/number-of-digit-one/

class Solution {
public:
    int countDigitOne(int n) {
        long long count = 0;
        long long factor = 1;
        long long value = n;
        while (factor <= value) {
            long long lower = value % factor;
            long long current = (value / factor) % 10;
            long long higher = value / (factor * 10);
            if (current == 0) {
                count += higher * factor;
            } else if (current == 1) {
                count += higher * factor + lower + 1;
            } else {
                count += (higher + 1) * factor;
            }
            factor *= 10;
        }
        return static_cast<int>(count);
    }
};
