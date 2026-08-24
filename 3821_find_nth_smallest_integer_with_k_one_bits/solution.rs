// LeetCode 3821 - Find Nth Smallest Integer With K One Bits
// https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/

impl Solution {
    pub fn nth_smallest(n: i64, k: i32) -> i64 {
        const MX: usize = 50;
        let mut c = [[0i64; MX + 1]; MX];
        for i in 0..MX {
            c[i][0] = 1;
            for j in 1..=i {
                c[i][j] = c[i - 1][j - 1] + c[i - 1][j];
            }
        }
        let mut n = n;
        let mut k = k as usize;
        let mut ans = 0i64;
        for i in (0..50).rev() {
            if n > c[i][k] {
                n -= c[i][k];
                ans |= 1i64 << i;
                k -= 1;
                if k == 0 {
                    break;
                }
            }
        }
        ans
    }
}
