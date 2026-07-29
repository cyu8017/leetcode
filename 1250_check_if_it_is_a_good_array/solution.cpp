// LeetCode 1250 - Check If It Is a Good Array
// https://leetcode.com/problems/check-if-it-is-a-good-array/

#include <numeric>
#include <vector>

class Solution {
public:
    bool isGoodArray(std::vector<int>& nums) {
        int g = nums[0];
        for (int x : nums) {
            g = std::gcd(g, x);
        }
        return g == 1;
    }
};
