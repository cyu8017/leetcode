// LeetCode 0698 - Partition to K Equal Sum Subsets
// https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

impl Solution {
    pub fn can_partition_k_subsets(mut nums: Vec<i32>, k: i32) -> bool {
        let total: i32 = nums.iter().sum();
        if total % k != 0 {
            return false;
        }
        let target = total / k;
        nums.sort_unstable_by(|a, b| b.cmp(a));
        if nums[0] > target {
            return false;
        }
        let mut buckets = vec![0; k as usize];
        Self::dfs(&nums, &mut buckets, 0, target)
    }

    fn dfs(nums: &[i32], buckets: &mut [i32], index: usize, target: i32) -> bool {
        if index == nums.len() {
            return true;
        }
        for i in 0..buckets.len() {
            if buckets[i] + nums[index] > target {
                continue;
            }
            buckets[i] += nums[index];
            if Self::dfs(nums, buckets, index + 1, target) {
                return true;
            }
            buckets[i] -= nums[index];
            if buckets[i] == 0 {
                break;
            }
        }
        false
    }
}
