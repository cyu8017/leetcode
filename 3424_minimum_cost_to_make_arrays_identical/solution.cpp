// LeetCode 3424 - Minimum Cost to Make Arrays Identical
// https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/

#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <vector>

class Solution {
public:
    long long minCost(std::vector<int>& arr, std::vector<int>& brr, long long k) {
        long long noSwap = 0;
        for (int i = 0; i < (int)arr.size(); i++) noSwap += std::abs(arr[i] - brr[i]);
        std::vector<int> a2 = arr, b2 = brr;
        std::sort(a2.begin(), a2.end());
        std::sort(b2.begin(), b2.end());
        long long withSwap = k;
        for (int i = 0; i < (int)a2.size(); i++) withSwap += std::abs(a2[i] - b2[i]);
        return noSwap < withSwap ? noSwap : withSwap;
    }
};
