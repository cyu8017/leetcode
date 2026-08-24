struct Solution;
// LeetCode 3969 - Valid Subarrays With Matching Sum Digits I
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/

impl Solution {
    pub fn count_valid_subarrays(nums: Vec<i32>, x: i32) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for l in 0..n {
            let mut s = 0i64;
            for r in l..n {
                s += nums[r] as i64;
                if s % 10 == x as i64 {
                    let t = s.to_string();
                    if t.as_bytes()[0] - b'0' == x as u8 {
                        ans += 1;
                    }
                }
            }
        }
        ans
    }
}

fn main() {}
