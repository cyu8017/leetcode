struct Solution;
// LeetCode 3979 - Maximum Valid Pair Sum
// https://leetcode.com/problems/maximum-valid-pair-sum/

impl Solution {
    pub fn max_valid_pair_sum(nums: Vec<i32>, k: i32) -> i32 {
        let mut ans = 0;
        let mut x = 0;
        for j in k as usize..nums.len() {
            let y = nums[j];
            x = x.max(nums[j - k as usize]);
            ans = ans.max(x + y);
        }
        ans
    }
}

fn main() {}
