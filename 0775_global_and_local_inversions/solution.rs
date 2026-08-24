// LeetCode 0775 - Global and Local Inversions
// https://leetcode.com/problems/global-and-local-inversions/

impl Solution {
    pub fn is_ideal_permutation(nums: Vec<i32>) -> bool {
        nums.iter()
            .enumerate()
            .all(|(i, &num)| (num - i as i32).abs() <= 1)
    }
}
