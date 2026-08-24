// LeetCode 3736 - Minimum Moves to Equal Array Elements III
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

impl Solution {
    pub fn min_moves(nums: Vec<i32>) -> i32 {
        let mut mx = 0;
        let mut s = 0;
        for &x in &nums {
            mx = mx.max(x);
            s += x;
        }
        mx * nums.len() as i32 - s
    }
}
