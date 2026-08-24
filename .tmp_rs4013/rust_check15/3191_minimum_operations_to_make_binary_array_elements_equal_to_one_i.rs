struct Solution;
// LeetCode 3191 - Minimum Operations to Make Binary Array Elements Equal to One I
// https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

impl Solution {
    pub fn min_operations(mut nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        let n = nums.len();
        for i in 0..n {
            if nums[i] == 0 {
                if i + 2 >= n {
                    return -1;
                }
                nums[i + 1] ^= 1;
                nums[i + 2] ^= 1;
                ans += 1;
            }
        }
        ans
    }
}

fn main() {}
