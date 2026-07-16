// LeetCode 0045 - Jump Game II
// https://leetcode.com/problems/jump-game-ii/

impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        let mut jumps = 0;
        let mut current_end = 0usize;
        let mut farthest = 0;

        for i in 0..nums.len() - 1 {
            farthest = farthest.max(i as i32 + nums[i]);
            if i == current_end {
                jumps += 1;
                current_end = farthest as usize;
            }
        }

        jumps
    }
}
