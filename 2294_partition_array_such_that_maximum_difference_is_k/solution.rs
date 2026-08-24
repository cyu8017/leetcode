// LeetCode 2294 - Partition Array Such That Maximum Difference Is K
// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

impl Solution {
    pub fn partition_array(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_unstable();
        let mut ans = 1;
        let mut start = nums[0];
        for &x in nums.iter().skip(1) {
            if x - start > k {
                ans += 1;
                start = x;
            }
        }
        ans
    }
}
