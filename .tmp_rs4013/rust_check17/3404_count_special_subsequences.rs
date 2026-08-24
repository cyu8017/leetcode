struct Solution;
// LeetCode 3404 - Count Special Subsequences
// https://leetcode.com/problems/count-special-subsequences/

impl Solution {
    pub fn number_of_subsequences(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut ans = 0i64;
        for i in 0..n {
            for j in (i + 2)..n {
                for k in (j + 2)..n {
                    for l in (k + 2)..n {
                        if nums[i] as i64 * nums[k] as i64 == nums[j] as i64 * nums[l] as i64 {
                            ans += 1;
                        }
                    }
                }
            }
        }
        ans
    }
}

fn main() {}
