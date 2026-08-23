// LeetCode 3115 - Maximum Prime Difference
// https://leetcode.com/problems/maximum-prime-difference/

#include <vector>

class Solution {
    static bool isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i <= n / i; i++)
            if (n % i == 0) return false;
        return true;
    }
public:
    int maximumPrimeDifference(std::vector<int>& nums) {
        for (int i = 0; ; i++) {
            if (isPrime(nums[i])) {
                for (int j = (int)nums.size() - 1; ; j--) {
                    if (isPrime(nums[j])) return j - i;
                }
            }
        }
    }
};
