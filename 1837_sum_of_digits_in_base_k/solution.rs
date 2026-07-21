// LeetCode 1837 - Sum of Digits in Base K
// https://leetcode.com/problems/sum-of-digits-in-base-k/

impl Solution {
    pub fn sum_base(mut n: i32, k: i32) -> i32 {
        let mut total = 0;
        while n > 0 {
            total += n % k;
            n /= k;
        }
        total
    }
}
