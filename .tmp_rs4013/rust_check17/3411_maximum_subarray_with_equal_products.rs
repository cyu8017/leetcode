struct Solution;
// LeetCode 3411 - Maximum Subarray With Equal Products
// https://leetcode.com/problems/maximum-subarray-with-equal-products/

impl Solution {
    fn gcd(mut a: i32, mut b: i32) -> i32 {
        while b != 0 {
            let t = a % b;
            a = b;
            b = t;
        }
        a
    }

    pub fn max_length(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 1;
        for i in 0..n {
            let mut prod = 1i64;
            let mut g = 0;
            let mut l = 1;
            for j in i..n {
                if prod > 1_000_000_000 / nums[j] as i64 {
                    break;
                }
                prod *= nums[j] as i64;
                if g == 0 {
                    g = nums[j];
                    l = nums[j];
                } else {
                    g = Self::gcd(g, nums[j]);
                    l = l / Self::gcd(l, nums[j]) * nums[j];
                }
                if prod == l as i64 * g as i64 && (j - i + 1) as i32 > ans {
                    ans = (j - i + 1) as i32;
                }
            }
        }
        ans
    }
}

fn main() {}
