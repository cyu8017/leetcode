// LeetCode 0698 - Partition to K Equal Sum Subsets
// https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
    std::vector<int> nums_;
    std::vector<int> buckets_;
    int target_ = 0;

    bool dfs(int index) {
        if (index == static_cast<int>(nums_.size())) {
            return true;
        }
        for (int i = 0; i < static_cast<int>(buckets_.size()); ++i) {
            if (buckets_[i] + nums_[index] > target_) {
                continue;
            }
            buckets_[i] += nums_[index];
            if (dfs(index + 1)) {
                return true;
            }
            buckets_[i] -= nums_[index];
            if (buckets_[i] == 0) {
                break;
            }
        }
        return false;
    }

public:
    bool canPartitionKSubsets(std::vector<int>& nums, int k) {
        const int total = std::accumulate(nums.begin(), nums.end(), 0);
        if (total % k != 0) {
            return false;
        }
        target_ = total / k;
        nums_ = nums;
        std::sort(nums_.begin(), nums_.end(), std::greater<int>());
        if (nums_[0] > target_) {
            return false;
        }
        buckets_.assign(k, 0);
        return dfs(0);
    }
};
