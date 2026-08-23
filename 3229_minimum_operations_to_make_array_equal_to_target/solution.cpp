// LeetCode 3229 - Minimum Operations to Make Array Equal to Target
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/

#include <vector>
#include <cstdlib>

class Solution {
public:
    long long minimumOperations(std::vector<int>& nums, std::vector<int>& target) {
        auto absv = [](int x) { return x < 0 ? -x : x; };
        long long f = absv(target[0] - nums[0]);
        for (int i = 1; i < (int)target.size(); i++) {
            int x = target[i] - nums[i];
            int y = target[i - 1] - nums[i - 1];
            if (1LL * x * y > 0) {
                int d = absv(x) - absv(y);
                if (d > 0) f += d;
            } else {
                f += absv(x);
            }
        }
        return f;
    }
};
