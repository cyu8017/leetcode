struct Solution;
// LeetCode 3848 - Check Digitorial Permutation
// https://leetcode.com/problems/check-digitorial-permutation/

impl Solution {
    pub fn is_digitorial_permutation(n: i32) -> bool {
        let mut f = [0i32; 10];
        f[0] = 1;
        for i in 1..10 {
            f[i] = f[i - 1] * i as i32;
        }
        let mut x = 0;
        let mut y = n;
        while y > 0 {
            x += f[(y % 10) as usize];
            y /= 10;
        }
        let mut a: Vec<u8> = x.to_string().into_bytes();
        let mut b: Vec<u8> = n.to_string().into_bytes();
        a.sort_unstable();
        b.sort_unstable();
        a == b
    }
}
