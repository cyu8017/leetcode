// LeetCode 3125 - Maximum Number That Makes Result of Bitwise AND Zero
// https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/

long long maxNumber(long long n) {
    int len = 0;
    unsigned long long x = (unsigned long long)n;
    while (x) { len++; x >>= 1; }
    return (1LL << (len - 1)) - 1;
}
