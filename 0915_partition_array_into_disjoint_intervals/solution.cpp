// LeetCode 0915 - Partition Array into Disjoint Intervals
// https://leetcode.com/problems/partition-array-into-disjoint-intervals/

#include <algorithm>
#include <vector>

class Solution {
public:
    int partitionDisjoint(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> minRight(n);
        minRight[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) minRight[i] = std::min(nums[i], minRight[i + 1]);
        int maxLeft = nums[0];
        for (int i = 1; i < n; i++) {
            if (maxLeft <= minRight[i]) return i;
            maxLeft = std::max(maxLeft, nums[i]);
        }
        return n - 1;
    }
};
