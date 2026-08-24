// LeetCode 2134 - Minimum Swaps to Group All 1's Together II
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

impl Solution {
    pub fn min_swaps(nums: Vec<i32>) -> i32 {
        let ones: i32 = nums.iter().sum();
        if ones == 0 {
            return 0;
        }
        let n = nums.len();
        let ones_u = ones as usize;
        let mut window: i32 = nums[..ones_u].iter().sum();
        let mut best = window;
        for i in 0..n {
            window -= nums[i];
            window += nums[(i + ones_u) % n];
            best = best.max(window);
        }
        ones - best
    }
}
