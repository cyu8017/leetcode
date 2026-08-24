// LeetCode 2023 - Number of Pairs of Strings With Concatenation Equal to Target
// https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

impl Solution {
    pub fn num_of_pairs(nums: Vec<String>, target: String) -> i32 {
        let mut ans = 0;
        for i in 0..nums.len() {
            for j in 0..nums.len() {
                if i != j && format!("{}{}", nums[i], nums[j]) == target {
                    ans += 1;
                }
            }
        }
        ans
    }
}
