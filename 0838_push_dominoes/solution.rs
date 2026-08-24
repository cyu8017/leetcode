// LeetCode 0838 - Push Dominoes
// https://leetcode.com/problems/push-dominoes/

impl Solution {
    pub fn push_dominoes(dominoes: String) -> String {
        let n = dominoes.len();
        let mut chars: Vec<u8> = dominoes.into_bytes();
        let mut force = vec![0i32; n];
        let mut f = 0i32;
        for i in 0..n {
            if chars[i] == b'R' {
                f = n as i32;
            } else if chars[i] == b'L' {
                f = 0;
            } else {
                f = (f - 1).max(0);
            }
            force[i] += f;
        }
        f = 0;
        for i in (0..n).rev() {
            if chars[i] == b'L' {
                f = n as i32;
            } else if chars[i] == b'R' {
                f = 0;
            } else {
                f = (f - 1).max(0);
            }
            force[i] -= f;
        }
        for i in 0..n {
            chars[i] = if force[i] > 0 {
                b'R'
            } else if force[i] < 0 {
                b'L'
            } else {
                b'.'
            };
        }
        String::from_utf8(chars).unwrap()
    }
}
