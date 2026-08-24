struct Solution;
// LeetCode 3334 - Find the Maximum Factor Score of Array
// https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

impl Solution {
    fn gcd(mut a: i64, mut b: i64) -> i64 {
        while b != 0 {
            let t = a % b;
            a = b;
            b = t;
        }
        a
    }
    fn lcm(a: i64, b: i64) -> i64 {
        a / Self::gcd(a, b) * b
    }

    pub fn max_score(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut gcd_all = nums[0] as i64;
        let mut lcm_all = nums[0] as i64;
        for i in 1..n {
            gcd_all = Self::gcd(gcd_all, nums[i] as i64);
            lcm_all = Self::lcm(lcm_all, nums[i] as i64);
        }
        let mut ans = gcd_all * lcm_all;
        for skip in 0..n {
            let mut g = 0i64;
            let mut l = 1i64;
            let mut first = true;
            for i in 0..n {
                if i == skip {
                    continue;
                }
                if first {
                    g = nums[i] as i64;
                    l = nums[i] as i64;
                    first = false;
                } else {
                    g = Self::gcd(g, nums[i] as i64);
                    l = Self::lcm(l, nums[i] as i64);
                }
            }
            if first {
                continue;
            }
            let v = g * l;
            if v > ans {
                ans = v;
            }
        }
        ans
    }
}

fn main() {}
