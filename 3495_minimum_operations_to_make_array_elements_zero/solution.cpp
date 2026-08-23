// LeetCode 3495 - Minimum Operations to Make Array Elements Zero
// https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

#include <vector>

class Solution {
    int opsToZero(int x) {
        int ops = 0;
        while (x > 0) { x /= 4; ops++; }
        return ops;
    }
public:
    long long minOperations(std::vector<std::vector<int>>& queries) {
        long long ans = 0;
        for (auto& q : queries) {
            int l = q[0], r = q[1];
            long long sum = 0;
            for (int x = l; x <= r; x++) sum += opsToZero(x);
            ans += (sum + 1) / 2;
        }
        return ans;
    }
};
