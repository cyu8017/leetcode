// LeetCode 3091 - Apply Operations to Make Sum of Array Greater Than or Equal to k
// https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/

#include <algorithm>

class Solution {
public:
    int minOperations(int k) {
        int ans = k;
        for (int a = 0; a < k; a++) {
            int x = a + 1;
            int b = (k + x - 1) / x - 1;
            ans = std::min(ans, a + b);
        }
        return ans;
    }
};
