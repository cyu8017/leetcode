// LeetCode 2521 - Distinct Prime Factors of Product of Array
// https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int distinctPrimeFactors(std::vector<int>& nums) {
        std::unordered_set<int> set;
        for (int x : nums) {
            for (int p = 2; p * p <= x; p++) {
                if (x % p == 0) {
                    set.insert(p);
                    while (x % p == 0) x /= p;
                }
            }
            if (x > 1) set.insert(x);
        }
        return (int)set.size();
    }
};
