// LeetCode 3659 - Partition Array Into K-Distinct Groups
// https://leetcode.com/problems/partition-array-into-k-distinct-groups/

#include <algorithm>
#include <vector>

class Solution {
public:
    bool partitionArray(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        if (n % k != 0) return false;
        int m = n / k;
        int mx = *std::max_element(nums.begin(), nums.end());
        std::vector<int> cnt(mx + 1);
        for (int x : nums)
            if (++cnt[x] > m) return false;
        return true;
    }
};
