// LeetCode 3628 - Maximum Number of Subsequences After One Inserting
// https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/

impl Solution {
    pub fn num_of_subsequences(s: String) -> i64 {
        let bytes = s.as_bytes();
        let calc = |t: &[u8; 2]| -> i64 {
            let mut cnt = 0i64;
            let mut a = 0i64;
            for &c in bytes {
                if c == t[1] {
                    cnt += a;
                }
                if c == t[0] {
                    a += 1;
                }
            }
            cnt
        };
        let mut r = bytes.iter().filter(|&&c| c == b'T').count() as i64;
        let mut l = 0i64;
        let mut ans = 0i64;
        let mut mx = 0i64;
        for &c in bytes {
            if c == b'T' {
                r -= 1;
            }
            if c == b'C' {
                ans += l * r;
            }
            if c == b'L' {
                l += 1;
            }
            mx = mx.max(l * r);
        }
        mx = mx.max(calc(b"LC")).max(calc(b"CT"));
        ans + mx
    }
}
