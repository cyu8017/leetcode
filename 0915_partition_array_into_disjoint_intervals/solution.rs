// LeetCode 0915 - Partition Array into Disjoint Intervals
// https://leetcode.com/problems/partition-array-into-disjoint-intervals/

impl Solution {
    pub fn partition_disjoint(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut min_right = vec![0; n];
        min_right[n - 1] = nums[n - 1];
        for i in (0..n - 1).rev() {
            min_right[i] = nums[i].min(min_right[i + 1]);
        }
        let mut max_left = nums[0];
        for i in 1..n {
            if max_left <= min_right[i] {
                return i as i32;
            }
            max_left = max_left.max(nums[i]);
        }
        (n - 1) as i32
    }
}
