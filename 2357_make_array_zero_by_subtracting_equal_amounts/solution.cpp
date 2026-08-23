// LeetCode 2357 - Make Array Zero by Subtracting Equal Amounts
// https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int minimumOperations(std::vector<int>& nums) {
        std::unordered_set<int> seen;
        for (int x : nums) {
            if (x > 0) seen.insert(x);
        }
        return (int)seen.size();
    }
};
