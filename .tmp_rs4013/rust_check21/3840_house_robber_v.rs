struct Solution;
// LeetCode 3840 - House Robber V
// https://leetcode.com/problems/house-robber-v/

impl Solution {
    pub fn rob(nums: Vec<i32>, colors: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut f = 0i64;
        let mut g = nums[0] as i64;
        for i in 1..n {
            if colors[i - 1] == colors[i] {
                let nf = f.max(g);
                g = f + nums[i] as i64;
                f = nf;
            } else {
                let nf = f.max(g);
                g = nf + nums[i] as i64;
                f = nf;
            }
        }
        f.max(g)
    }
}
