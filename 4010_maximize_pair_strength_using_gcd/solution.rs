// LeetCode 4010 - Maximize Pair Strength Using GCD
// https://leetcode.com/problems/maximize-pair-strength-using-gcd/

fn gcd(mut a: i64, mut b: i64) -> i64 {
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

impl Solution {
    pub fn max_pair_strength(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut ans = 0i64;
        for i in 0..n {
            for j in (i + 1)..n {
                let g = gcd(nums[i] as i64, nums[j] as i64);
                let x = nums[i] as i64 * nums[j] as i64 / (g * g);
                ans = ans.max(x);
            }
        }
        ans
    }
}
