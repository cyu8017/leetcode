// LeetCode 2495 - Number of Subarrays Having Even Product
// https://leetcode.com/problems/number-of-subarrays-having-even-product/

#include <vector>

class Solution {
public:
    long long evenProduct(std::vector<int>& nums) {
        long long n = (long long)nums.size();
        long long total = n * (n + 1) / 2;
        long long oddLen = 0, odd = 0;
        for (int x : nums) {
            if (x % 2 == 1) {
                odd++;
                oddLen += odd;
            } else {
                odd = 0;
            }
        }
        return total - oddLen;
    }
};
