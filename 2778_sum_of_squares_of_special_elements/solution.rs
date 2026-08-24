// LeetCode 2778 - Sum of Squares of Special Elements
// https://leetcode.com/problems/sum-of-squares-of-special-elements/

impl Solution {
    pub fn sum_of_squares(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let mut ans = 0;
        for (i, &v) in nums.iter().enumerate() {
            if n % (i as i32 + 1) == 0 {
                ans += v * v;
            }
        }
        ans
    }
}
