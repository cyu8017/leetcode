// LeetCode 0762 - Prime Number of Set Bits in Binary Representation
// https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

#include <unordered_set>

class Solution {
public:
    int countPrimeSetBits(int left, int right) {
        static const std::unordered_set<int> primes{2, 3, 5, 7, 11, 13, 17, 19};
        int ans = 0;
        for (int num = left; num <= right; ++num) {
            if (primes.count(__builtin_popcount(num))) {
                ++ans;
            }
        }
        return ans;
    }
};
