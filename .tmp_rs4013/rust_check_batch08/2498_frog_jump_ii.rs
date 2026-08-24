struct Solution;
// LeetCode 2498 - Frog Jump II
// https://leetcode.com/problems/frog-jump-ii/

impl Solution {
    pub fn max_jump(stones: Vec<i32>) -> i32 {
        let mut ans = stones[1] - stones[0];
        for i in 2..stones.len() {
            let diff = stones[i] - stones[i - 2];
            if diff > ans {
                ans = diff;
            }
        }
        ans
    }
}

fn main() {}
