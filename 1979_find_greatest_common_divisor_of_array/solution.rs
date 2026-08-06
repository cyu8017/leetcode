// LeetCode 1979 - Find Greatest Common Divisor of Array
// https://leetcode.com/problems/find-greatest-common-divisor-of-array/

impl Solution {
    pub fn find_gcd(nums: Vec<i32>) -> i32 {
        let mut a = *nums.iter().min().unwrap();
        let mut b = *nums.iter().max().unwrap();
        while b != 0 {
            let t = a % b;
            a = b;
            b = t;
        }
        a
    }
}
