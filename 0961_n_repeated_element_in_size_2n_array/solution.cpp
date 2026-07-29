// LeetCode 0961 - N-Repeated Element in Size 2N Array
// https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int repeatedNTimes(std::vector<int>& nums) {
        std::unordered_set<int> seen;
        for (int x : nums) {
            if (seen.count(x)) return x;
            seen.insert(x);
        }
        return -1;
    }
};
