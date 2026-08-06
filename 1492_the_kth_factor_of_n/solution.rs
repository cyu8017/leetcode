// LeetCode 1492 - The kth Factor of n
// https://leetcode.com/problems/the-kth-factor-of-n/

impl Solution {
    pub fn kth_factor(n: i32, mut k: i32) -> i32 {
        for x in 1..=n {
            if n % x == 0 {
                k -= 1;
                if k == 0 {
                    return x;
                }
            }
        }
        -1
    }
}
