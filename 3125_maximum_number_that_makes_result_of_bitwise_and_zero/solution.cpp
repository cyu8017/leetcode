// LeetCode 3125 - Maximum Number That Makes Result of Bitwise AND Zero
// https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/

class Solution {
public:
    long long maxNumber(long long n) {
        int len = 64 - __builtin_clzll((unsigned long long)n);
        return (1LL << (len - 1)) - 1;
    }
};
