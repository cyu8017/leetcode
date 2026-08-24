// LeetCode 0645 - Set Mismatch
// https://leetcode.com/problems/set-mismatch/

impl Solution {
    pub fn find_error_nums(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut seen = vec![0; n + 1];
        let mut duplicate = -1;
        let mut missing = -1;
        for value in nums {
            seen[value as usize] += 1;
        }
        for value in 1..=n {
            if seen[value] == 2 {
                duplicate = value as i32;
            } else if seen[value] == 0 {
                missing = value as i32;
            }
        }
        vec![duplicate, missing]
    }
}
