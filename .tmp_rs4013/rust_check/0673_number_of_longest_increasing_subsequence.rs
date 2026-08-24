struct Solution;
// LeetCode 0673 - Number of Longest Increasing Subsequence
// https://leetcode.com/problems/number-of-longest-increasing-subsequence/

impl Solution {
    pub fn find_number_of_lis(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut lengths = vec![1; n];
        let mut counts = vec![1; n];
        for i in 0..n {
            for j in 0..i {
                if nums[j] >= nums[i] {
                    continue;
                }
                if lengths[j] + 1 > lengths[i] {
                    lengths[i] = lengths[j] + 1;
                    counts[i] = counts[j];
                } else if lengths[j] + 1 == lengths[i] {
                    counts[i] += counts[j];
                }
            }
        }
        let longest = *lengths.iter().max().unwrap();
        counts
            .iter()
            .zip(lengths.iter())
            .filter(|(_, &len)| len == longest)
            .map(|(c, _)| *c)
            .sum()
    }
}

fn main() {}
