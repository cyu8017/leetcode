// LeetCode 1313 - Decompress Run-Length Encoded List
// https://leetcode.com/problems/decompress-run-length-encoded-list/

impl Solution {
    pub fn decompress_rl_elist(nums: Vec<i32>) -> Vec<i32> {
        let mut answer = Vec::new();
        let mut i = 0;
        while i < nums.len() {
            for _ in 0..nums[i] {
                answer.push(nums[i + 1]);
            }
            i += 2;
        }
        answer
    }
}
