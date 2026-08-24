struct Solution;
fn main() {}

// LeetCode 2824 - Count Pairs Whose Sum is Less than Target
// https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

impl Solution {
    pub fn count_pairs(nums: Vec<i32>, target: i32) -> i32 {
        let mut ans = 0;
        for i in 0..nums.len() {
            for j in i + 1..nums.len() {
                if nums[i] + nums[j] < target {
                    ans += 1;
                }
            }
        }
        ans
    }
}
