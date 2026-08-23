// LeetCode 2441 - Largest Positive Integer That Exists With Its Negative
// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int findMaxK(std::vector<int>& nums) {
        std::unordered_set<int> seen;
        int ans = -1;
        for (int x : nums) {
            seen.insert(x);
            if (x > 0 && seen.count(-x) && x > ans) ans = x;
            if (x < 0 && seen.count(-x) && -x > ans) ans = -x;
        }
        return ans;
    }
};
