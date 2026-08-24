struct Solution;
// LeetCode 3827 - Count Monobit Integers
// https://leetcode.com/problems/count-monobit-integers/

impl Solution {
    pub fn count_monobit(n: i32) -> i32 {
        let mut ans = 1;
        let mut i = 1;
        let mut x = 1i32;
        while x <= n {
            ans += 1;
            x += 1 << i;
            i += 1;
        }
        ans
    }
}
