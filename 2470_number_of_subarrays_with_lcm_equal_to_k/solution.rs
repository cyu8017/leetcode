// LeetCode 2470 - Number of Subarrays With LCM Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

impl Solution {
    pub fn subarray_lcm(nums: Vec<i32>, k: i32) -> i32 {
        fn gcd(mut x: i64, mut y: i64) -> i64 {
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
            let mut cur = 1i64;
            for j in i..n {
                let x = nums[j] as i64;
                cur = cur / gcd(cur, x) * x;
                if cur > k as i64 {
                    break;
                }
                if cur == k as i64 {
                    ans += 1;
                }
            }
        }
        ans
    }
}
