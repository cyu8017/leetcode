// LeetCode 2600 - K Items With the Maximum Sum
// https://leetcode.com/problems/k-items-with-the-maximum-sum/

#include <algorithm>

class Solution {
public:
    int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        int ans = 0;
        int take = std::min(numOnes, k);
        ans += take;
        k -= take;
        take = std::min(numZeros, k);
        k -= take;
        take = std::min(numNegOnes, k);
        ans -= take;
        return ans;
    }
};
