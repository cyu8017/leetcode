// LeetCode 1979 - Find Greatest Common Divisor of Array
#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int findGCD(std::vector<int>& nums) {
        int a = *std::min_element(nums.begin(), nums.end());
        int b = *std::max_element(nums.begin(), nums.end());
        return std::gcd(a, b);
    }
};
