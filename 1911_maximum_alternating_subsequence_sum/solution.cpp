// LeetCode 1911 - Maximum Alternating Subsequence Sum
// https://leetcode.com/problems/maximum-alternating-subsequence-sum/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxAlternatingSum(std::vector<int>& nums) {
        long long even = 0, odd = 0;
        for (int x : nums) {
            long long ne = std::max(even, odd + x);
            long long no = std::max(odd, even - x);
            even = ne;
            odd = no;
        }
        return even;
    }
};
