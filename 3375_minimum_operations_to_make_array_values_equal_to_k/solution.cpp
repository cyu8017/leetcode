// LeetCode 3375 - Minimum Operations to Make Array Values Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums, int k) {
        std::unordered_set<int> seen;
        for (int x : nums) {
            if (x < k) return -1;
            if (x > k) seen.insert(x);
        }
        return (int)seen.size();
    }
};
