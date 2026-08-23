// LeetCode 3644 - Maximum K to Sort a Permutation
// https://leetcode.com/problems/maximum-k-to-sort-a-permutation/

#include <algorithm>
#include <vector>

class Solution {
public:
    int sortPermutation(std::vector<int>& nums) {
        int ans = -1;
        for (int i = 0; i < (int)nums.size(); i++)
            if (i != nums[i]) ans &= nums[i];
        return std::max(ans, 0);
    }
};
