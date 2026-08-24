struct Solution;
// LeetCode 3867 - Sum of GCD of Formed Pairs
// https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

impl Solution {
    pub fn gcd_sum(nums: Vec<i32>) -> i64 {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        let n = nums.len();
        let mut prefix_gcd = vec![0; n];
        let mut mx = 0;
        for i in 0..n {
            mx = mx.max(nums[i]);
            prefix_gcd[i] = gcd(nums[i], mx);
        }
        prefix_gcd.sort_unstable();
        let mut ans = 0i64;
        for i in 0..n / 2 {
            ans += gcd(prefix_gcd[i], prefix_gcd[n - i - 1]) as i64;
        }
        ans
    }
}
