struct Solution;
// LeetCode 2447 - Number of Subarrays With GCD Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

impl Solution {
    pub fn subarray_gcd(nums: Vec<i32>, k: i32) -> i32 {
        fn gcd(mut x: i32, mut y: i32) -> i32 {
            while y != 0 {
                let t = x % y;
                x = y;
                y = t;
            }
            x
        }
        let mut ans = 0;
        let n = nums.len();
        for i in 0..n {
            let mut g = 0;
            for j in i..n {
                g = gcd(g, nums[j]);
                if g < k {
                    break;
                }
                if g == k {
                    ans += 1;
                }
            }
        }
        ans
    }
}

fn main() {}
