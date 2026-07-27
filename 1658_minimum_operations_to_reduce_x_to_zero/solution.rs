// LeetCode 1658 - Minimum Operations to Reduce X to Zero
// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

impl Solution {
    pub fn min_operations(nums: Vec<i32>, x: i32) -> i32 {
        let total: i32 = nums.iter().sum();
        let target = total - x;
        if target < 0 {
            return -1;
        }
        let mut best = -1;
        let mut left = 0usize;
        let mut cur = 0i32;
        for (right, &v) in nums.iter().enumerate() {
            cur += v;
            while cur > target {
                cur -= nums[left];
                left += 1;
            }
            if cur == target {
                best = best.max((right - left + 1) as i32);
            }
        }
        if best < 0 {
            -1
        } else {
            nums.len() as i32 - best
        }
    }
}
