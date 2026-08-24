// LeetCode 3178 - Find the Child Who Has the Ball After K Seconds
// https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/

impl Solution {
    pub fn number_of_child(n: i32, k: i32) -> i32 {
        let mut k = k;
        let m = k % (n - 1);
        k /= n - 1;
        if k % 2 == 1 {
            n - m - 1
        } else {
            m
        }
    }
}
